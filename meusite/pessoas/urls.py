from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('nova', views.nova, name='nova'),
    path('<int:pessoa_id>/editar', views.editar, name='editar')
]