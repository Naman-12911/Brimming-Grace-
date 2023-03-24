from django.urls import path
from .views import employeeAPIView
urlpatterns = [
    path("employe",employeeAPIView.as_view()),
    path('employe/<str:pk>', employeeAPIView.as_view()), # to capture our ids
    
]
