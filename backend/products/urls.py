from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    # detail api view takes one field as a lookup field, has to be pk (not id)
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/update', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ProductDestroyAPIView.as_view()),
    
]