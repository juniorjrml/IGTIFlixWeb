from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include('principal.urls')),
    path(route='principal/', view=include('principal.urls')),
    path(route='genero/', view=include('genero.urls')),
    path(route='serie/', view=include('serie.urls'))
]
