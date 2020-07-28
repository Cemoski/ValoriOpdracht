"""
Valori URL Configuration

"""
from django.urls import path
from .import views

urlpatterns = [
	path('api', views.apiOverview, name="api-overview"),
	path('intern-list/', views.internList, name="intern-list"),
	path('detail-intern/<str:pk>/', views.detailIntern, name="detail-intern"),
	path('create-intern/', views.createIntern, name="create-intern"),

	path('update-intern/<str:pk>/', views.updateIntern, name="update-intern"),
	path('delete-intern/<str:pk>/', views.deleteIntern, name="delete-intern"),
]