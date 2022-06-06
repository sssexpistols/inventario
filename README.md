# Inventario
Proyecto final en la materia de Algoritmos y estructura de datos

# Requisitos
``
  Tener python
``
## Instalación
```pip install Django==4.0.4```

## Secciones

En la sección Productos, es donde los usuarios de vista y eliminar datos podrán navegar, ya que como se menciona, solo podrán acceder a ver los productos y eliminarlos, sección de nosotros es una breve info sobre los desarrolladores y el menú los regresará a la plantilla principal


## Uso del inventario

Una vez configurada la DB en el archivo settings.py, ejecutar el comando

```python manage.py migrate```

Esto hará que la DB esté totalmente conectada con nuestro sistema

  Crear un superusuario que manejará, editará, creará y eliminará productos del inventario y su manejo con los proveedores, con el siguiente comando:

```python manage.py createsuperuser```

  Colocar los datos solicitados y con el usuario y su cotnraseña creada, podrá acceder a la url ```localhost:8000/admin``` para manejar todo lo antes mencionado.
  
 ### Listo!
