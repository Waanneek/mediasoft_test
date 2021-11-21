from django.urls import path, include
from api import views


urlpatterns = [
    # path('', views.City.as_view()),
    path('city/street/', views.StreetView.as_view()),
    path('city/', views.CityView.as_view()),
    path('shop/', views.ShopView.as_view()),

    ]