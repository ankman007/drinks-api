from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('drink-list/', views.drink_list, name='drink-list'),
    path('drink-detail/<str:pk>/', views.drink_detail, name='drink-detail'),
    path('drink-add/', views.drink_add, name='drink-add'),
    path('drink-update/<str:pk>/', views.drink_update, name='drink-update'),
    path('drink-delete/<str:pk>/', views.drink_delete, name='drink-delete'),
]