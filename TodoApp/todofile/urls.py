from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="ba"),
    path('delete/<list_id>',views.delete,name="delete"),
    path('cut/<list_id>',views.cut,name="cut"),
    path('uncut/<list_id>',views.uncut,name="uncut"),
    path('edit/<list_id>',views.edit,name="edit"),
]
