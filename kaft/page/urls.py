from django.urls import path
from .views import page_create, index


urlpatterns = [
    path('page/create', page_create, name='page_create'),
    path('page/', index),

]
