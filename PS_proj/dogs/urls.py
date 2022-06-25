from django.urls import path
from . import views

app_name = 'dogs'


urlpatterns = [
    path('dogs', views.dogs, name='dogs'),
    path('curators', views.curators, name='curators'),
    path('owners', views.owners, name='owners'),
    path('potential_owners', views.potential_owners, name='potential_owners'),
    path('add_dog', views.add_dog, name='add_dog'),
    path('add_curator', views.add_curator, name='add_curator'),
    path('add_owner', views.add_owner, name='add_owner'),
    path('add_adoption/<int:owner_id>/', views.add_adoption,
         name='add_adoption'
         ),
    path('edit_dog/<int:dog_id>/', views.edit_dog, name='edit_dog'),
    path('edit_curator/<int:curator_id>/', views.edit_curator,
         name='edit_curator'
         ),
    path('edit_owner/<int:owner_id>/', views.edit_owner, name='edit_owner'),
    path('audition/<int:owner_id>/', views.audition, name='audition'),
    path('owners_to_audit', views.owners_to_audit, name='owners_to_audit'),
    path('profile_dog/<int:dog_id>', views.profile_dog, name='profile_dog'),
    path('profile_curator/<int:curator_id>', views.profile_curator,
         name='profile_curator'
         ),
    path('profile_owner/<int:owner_id>', views.profile_owner,
         name='profile_owner'
         ),
    path('change_owner/<int:dog_id>/', views.change_owner,
         name='change_owner'
         )
]
