from django.contrib import admin
from invoiceApp import views
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('login/', TokenObtainPairView.as_view()),
    path('usuario/<int:pk>/', views.UsuarioRetrieveUpdateDeleteView.as_view()),    
    path('refresh/', TokenRefreshView.as_view()),
    path('cliente/', views.ClientListCreateView.as_view()),    
    path('cliente/<int:pk>/', views.ClienteRetrieveUpdateView.as_view()), 
    path('empleado/', views.EmpleadoListCreateView.as_view()),    
    path('empleado/<int:pk>/', views.EmpleadoRetrieveUpdateView.as_view()),
    path('proveedor/', views.ProveedorListCreateView.as_view()),    
    path('proveedor/<int:pk>/', views.ProveedorRetrieveUpdateView.as_view()),
    path('producto/', views.ProductoCreateView.as_view()),    
    path('producto/<int:pk>/', views.ProductoRetrieveUpdateDeleteView.as_view()),
    path('factura/', views.facturaListCreate),
    path('factura/<int:pk>/', views.facturaRetrieveDelete),
    path('compra/', views.CompraCreateView.as_view()),  
]








