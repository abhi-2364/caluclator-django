from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.html),
     path('calc',views.calc,name='calc')
]
