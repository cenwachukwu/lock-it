from django.urls import path, include
from views import notes_detail_view, notes_list

app_name = 'lock_it'

urlpatterns = [
    path('notes/', notes_list, name="list"),
    path('<slug>', notes_detail_view, name="detail"),
]