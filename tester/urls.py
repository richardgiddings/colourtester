from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_combo/', views.add_combo, name='add_combo'),
    path('edit_combo/<int:combo_id>/', views.edit_combo, name='edit_combo'),
]