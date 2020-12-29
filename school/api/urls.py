from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('student-list', views.studentList, name="student-list"),
	path('student-detail/<str:pk>/', views.studentDetail, name="student-detail"),
	path('student-create/', views.studentCreate, name="student-create"),
	path('student-update/<str:pk>/', views.studentUpdate, name="student-update"),
	path('student-delete/<str:pk>/', views.studentDelete, name="student-delete"),
]