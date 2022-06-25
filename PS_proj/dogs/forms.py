from django import forms
from .models import Dog, Curator, Owner, Adoption


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'
        labels = {
            'name': 'Кличка собаки',
            'curator': 'ФИО куратора'

        }
        help_texts = {
            'curator':
            'Если куратора нет в списке, необходимо сначала '
            'добавить его в каталог кураторов'
        }


class CuratorForm(forms.ModelForm):
    class Meta:
        model = Curator
        fields = '__all__'
        labels = {
            'name': 'ФИО куратора',
            'pound': 'Приют'

        }
        help_texts = {
            'name': 'ФИО куратора',
            'pound': 'Название приюта'
        }


class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'tel']


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['dog']


class EditOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class AuditForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['sobes_status', 'sobes_result']


class ChangeOwnerForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['dog', 'owner']
