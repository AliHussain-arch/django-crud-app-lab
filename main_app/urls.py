from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),  
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('cars/<int:car_id>/add-cleaning/', views.add_cleaning, name='add-cleaning'),
    path('cars/<int:car_id>/cleaning/<int:pk>/update/', views.CleaningUpdate.as_view(), name='update-cleaning'),
    path('cars/<int:car_id>/cleaning/<int:pk>/delete/', views.CleaningDelete.as_view(), name='delete-cleaning'),
]

