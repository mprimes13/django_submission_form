from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirmation/<int:entry_id>', views.confirmation, name='confirmation'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('submit', views.submit, name='submit')
]
