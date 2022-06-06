from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('medicamentos', views.productos, name='medicamentos'),
    path('medicamentos/crear', views.crear, name='crear'),
    path('medicamentos/editar', views.editar, name='editar'),
    path('form', views.formulario, name='form'),
    path('eliminar/<int:medicine_id>', views.eliminar, name='eliminar'),
]
