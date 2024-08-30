from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_alt_view),
    # detail api view takes one field as a lookup field, has to be pk (not id)
    path('<int:pk>/', views.product_alt_view),
    
]