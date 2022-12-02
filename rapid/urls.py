from django.urls import path
from .views import *

urlpatterns = [
    path('apply/', Apply.as_view()),
    path('personalinformation/', PersonalInformation.as_view()),
    path('universityselection/', UniversityInformation.as_view()),
    path('educationinformation/', EducationInformation.as_view()),
    path('uploaddocuments/', UploadDocumnts.as_view()),
]