from django.shortcuts import render, redirect, get_object_or_404
from core.paginator import paginator
from .models import Dog, Curator, Owner, Adoption
from .forms import (DogForm, CuratorForm, AddOwnerForm, ContractOwnerForm,
                    AuditForm, AdoptionForm, ChangeOwnerForm, EditOwnerForm,
                    ContractAdoptionForm)


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
        dog_owner__dog__isnull=True).filter(dog_owner__contract_signed=True)
    context = {
        'page_object': paginator(request, owners)
    }
    return render(request, 'dogs/owners.html', context)


def potential_owners(request):
    owners = Owner.objects.exclude(dog_owner__contract_signed=True)
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
    form_owner = AddOwnerForm(request.POST or None)
    if not request.method == 'POST' or not form_owner.is_valid():
        return render(
            request,
            'dogs/add_owner.html',
            {'form_owner': form_owner}
        )
    instance = form_owner.save(commit=False)
    form_owner.save()
    return redirect('dogs:add_adoption', instance.id)


def add_adoption(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    form_owner = AdoptionForm(request.POST or None)
    if not request.method == 'POST' or not form_owner.is_valid():
        context = {
            'form_owner': form_owner,
            'adopt': True
        }
        return render(request, 'dogs/add_owner.html', context)

    instance = form_owner.save(commit=False)
    instance.owner = owner
    form_owner.save()
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
    dogs = Dog.objects.filter(adopted_dog__owner=owner)
    form_owner = EditOwnerForm(
        request.POST or None,
        instance=owner
    )
    if form_owner.is_valid():
        form_owner.save()
        return redirect('dogs:owners')
    context = {
        'dogs': dogs,
        'is_edit': True,
        'form_owner': form_owner
    }
    return render(request, 'dogs/add_owner.html', context)


def audition(request, adoption_id):
    adoption = get_object_or_404(Adoption, id=adoption_id)
    dog = adoption.dog
    owner = adoption.owner
    form_adoption = AuditForm(
        request.POST or None,
        instance=adoption
    )
    if form_adoption.is_valid():
        form_adoption.save()
        return redirect('dogs:owners')
    context = {
        'owner': owner,
        'dog': dog,
        'audit': True,
        'form_adoption': form_adoption
    }
    return render(request, 'dogs/add_owner.html', context)


def owners_to_audit(request):
    adoptions = Adoption.objects.filter(
        sobes_status='Not_auditioned',
        contract_signed='False'
    )
    context = {
        'page_object': paginator(request, adoptions)
    }
    return render(request, 'dogs/owners_to_proceed.html', context)


def profile_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    try:
        owner = Owner.objects.filter(
            dog_owner__dog=dog,
            dog_owner__contract_signed=True
        ).get()
        adoption = Adoption.objects.get(owner=owner, dog=dog)
    except Owner.DoesNotExist:
        owner = False
        adoption = False
    context = {
        'dog': dog,
        'owner': owner,
        'adoption': adoption
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
    dogs = Dog.objects.filter(
        adopted_dog__owner=owner,
        adopted_dog__contract_signed=True
    )
    adoptions = Adoption.objects.filter(owner=owner)
    context = {
        'dogs': dogs,
        'owner': owner,
        'adoptions': adoptions
    }
    return render(request, 'dogs/profile_owner.html', context)


def change_owner(request, adoption_id):
    adoption = get_object_or_404(Adoption, id=adoption_id)
    form = ChangeOwnerForm(
        request.POST or None,
        instance=adoption
    )
    if not request.method == 'POST' or not form.is_valid():
        context = {
            'form': form,
            'adoption_id': adoption_id
        }
        return render(request, 'dogs/change_owner.html', context)
    form.save()
    return redirect('/')


def contract(request, adoption_id):
    adoption = get_object_or_404(Adoption, id=adoption_id)
    owner = adoption.owner
    form_owner = ContractOwnerForm(
        request.POST or None,
        instance=owner
    )
    form_adoption = ContractAdoptionForm(
        request.POST or None,
        instance=adoption
    )
    if (
        not request.method == 'POST'
        or not form_owner.is_valid()
        or not form_adoption.is_valid()
         ):
        context = {
            'form_owner': form_owner,
            'form_adoption': form_adoption,
            'dogs': dogs,
            'contract': True
        }
        return render(request, 'dogs/add_owner.html', context)
    form_owner.save()
    form_adoption.save()
    return redirect('/')


def adoptions_to_contract(request):
    adoptions = Adoption.objects.filter(contract_signed=False)
    context = {
        'page_object': paginator(request, adoptions)
    }
    return render(request, 'dogs/adoptions_to_proceed.html', context)


def adoption_info(request, adoption_id):
    adoption = get_object_or_404(Adoption, id=adoption_id)
    context = {
        'adoption': adoption
    }
    return render(request, 'dogs/adoption_info.html', context)
