from Ordering import api_views
from django.urls import path

urlpatterns = [

    path('User',api_views.UserCreateList.as_view()),

    path('User/<int:pk>',api_views.UserUpdateDelete.as_view()),

    path('Order',api_views.OrderCreateList.as_view()),

    path('Order/<int:pk>',api_views.OrderUpdateDelete.as_view()),
]



