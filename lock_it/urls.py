from django.urls import path, include
from lock_it.views import (notes_detail_view, 
    notes_list,
    notes_update_view,
    notes_delete_view,
    notes_create_view,
    registration_view,
)

app_name = 'lock_it'

urlpatterns = [
    path('notes/', notes_list, name="list"),
    path('notes/<slug>/', notes_detail_view, name="detail"),
    path('notes/<slug>/update', notes_update_view, name="update"),
    path('notes/<slug>/delete', notes_delete_view, name="delete"),
    path('create/', notes_create_view, name="create"),
    path('register/', registration_view, name="registration"),
]