from django.urls import path
from . import views

 

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('update_contact/<str:pk>/', views.updateContact, name="update_contact"),
    path('delete_contact/<str:pk>/', views.deleteContact, name="delete_contact"),
    path('search_name', views.searchName, name="search_name"),
    path('search_profession', views.searchProfession, name="search_profession"),
    path('compare_name', views.compareName, name="compare_name"),
]