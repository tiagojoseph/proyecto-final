from django.urls import path 
from inicio.views import inicio, crear_la_propiedad  

urlpatterns = [
    path ("", inicio),
    path ("crear-la-propiedad/<int:metros_cuadrados>/<str:ubicacion>/<str:precio>", crear_la_propiedad)
]