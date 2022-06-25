from django.shortcuts import render, redirect, get_object_or_404
from core.paginator import paginator
from .models import Dog, Curator, Owner, Adoption
from .forms import (DogForm, CuratorForm, AddOwnerForm, EditOwnerForm,
                    AuditForm, AdoptionForm, ChangeOwnerForm)


def dogs(request):
    dogs = Dog.objects.select_related('curator')
    context = {
        'page_object': paginator(request, dogs)
    }
    return render(request, 'dogs/dogs.html', context)


def curators(request):
    curators = Curator.objects.all()
    context = {
        'dogs': dogs,
        'page_object': paginator(request, curators)
    }
    return render(request, 'dogs/curators.html', context)


def owners(request):
    owners = Owner.objects.exclude(
        dog_owner__dog__isnull=True).filter(sobes_status='OK')
    context = {
        'page_object': paginator(request, owners)
    }
    return render(request, 'dogs/owners.html', context)


def potential_owners(request):
    owners = Owner.objects.exclude(sobes_status='OK')
    context = {
        'potential': True,
        'page_object': paginator(request, owners)
    }
    return render(request, 'dogs/owners.html', context)


def add_dog(request):
    form = DogForm(
        request.POST or None
    )
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'dogs/add_dog.html', {'form': form})
    form.save()
    return redirect('dogs:dogs')


def add_curator(request):
    form = CuratorForm(
        request.POST or None
    )
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'dogs/add_curator.html', {'form': form})
    form.save()
    return redirect('dogs:dogs')


def add_owner(request):
    form = AddOwnerForm(request.POST or None)
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'dogs/add_owner.html', {'form': form})
    instance = form.save(commit=False)
    form.save()
    return redirect('dogs:add_adoption', instance.id)


def add_adoption(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    form = AdoptionForm(request.POST or None)
    if not request.method == 'POST' or not form.is_valid():
        context = {
            'form': form,
            'adopt': True
        }
        return render(request, 'dogs/add_owner.html', context)

    instance = form.save(commit=False)
    instance.owner = owner
    form.save()
    return redirect('/')


def edit_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    form = DogForm(
        request.POST or None,
        instance=dog
    )
    if form.is_valid():
        form.save()
        return redirect('dogs:dogs')
    context = {
        'is_edit': True,
        'form': form
    }
    return render(request, 'dogs/add_dog.html', context)


def edit_curator(request, curator_id):
    curator = get_object_or_404(Curator, id=curator_id)
    form = CuratorForm(
        request.POST or None,
        instance=curator
    )
    if form.is_valid():
        form.save()
        return redirect('dogs:curators')
    context = {
        'is_edit': True,
        'form': form
    }
    return render(request, 'dogs/add_curator.html', context)


def edit_owner(request, owner_id):
    owner = get_object_or_404(Owner, id=owner_id)
    try:
        dog = Dog.objects.get(adopted_dog__owner=owner)
    except Dog.DoesNotExist:
        dog = False
    form = EditOwnerForm(
        request.POST or None,
        instance=owner
    )
    if form.is_valid():
        form.save()
        return redirect('dogs:owners')
    context = {
        'dog': dog,
        'is_edit': True,
        'form': form
    }
    return render(request, 'dogs/add_owner.html', context)


def audition(request, owner_id):
    owner = get_object_or_404(Owner, id=owner_id)
    try:
        dog = Dog.objects.get(adopted_dog__owner=owner)
    except Dog.DoesNotExist:
        dog = False
    form = AuditForm(
        request.POST or None,
        instance=owner
    )
    if form.is_valid():
        form.save()
        return redirect('dogs:owners')
    context = {
        'owner': owner,
        'dog': dog,
        'audit': True,
        'form': form
    }
    return render(request, 'dogs/add_owner.html', context)


def owners_to_audit(request):
    owners = Owner.objects.filter(sobes_status='Not_auditioned')
    context = {
        'page_object': paginator(request, owners)
    }
    return render(request, 'dogs/owners_to_audit.html', context)


def profile_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    try:
        owner = Owner.objects.filter(dog_owner__dog=dog).get()
    except Owner.DoesNotExist:
        owner = False
    context = {
        'dog': dog,
        'owner': owner
    }
    return render(request, 'dogs/profile_dog.html', context)


def profile_curator(request, curator_id):
    curator = get_object_or_404(Curator, id=curator_id)
    dogs = curator.curator.select_related('curator')
    context = {
        'dogs': dogs,
        'curator': curator
    }
    return render(request, 'dogs/profile_curator.html', context)


def profile_owner(request, owner_id):
    owner = get_object_or_404(Owner, id=owner_id)
    try:
        legitimate = (Dog.objects.filter(adopted_dog__owner=owner).get()
                      and owner.sobes_status == 'OK')
    except Dog.DoesNotExist:
        legitimate = False
    context = {
        'legitimate': legitimate,
        'owner': owner
    }
    return render(request, 'dogs/profile_owner.html', context)


def change_owner(request, dog_id):
    adoption = get_object_or_404(Adoption, dog=dog_id)
    form = ChangeOwnerForm(
        request.POST or None,
        instance=adoption
    )
    if not request.method == 'POST' or not form.is_valid():
        context = {
            'form': form,
            'dog_id': dog_id
        }
        return render(request, 'dogs/change_owner.html', context)
    form.save()
    return redirect('/')
