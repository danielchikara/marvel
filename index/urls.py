from django.urls import path
from .views import home
urlpatterns = [
    path('', home, name='home'),  # URL para la página de inicio
    path('test/', home,name='comic')
]
