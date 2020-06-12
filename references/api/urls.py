from django.urls import path
from . import views

app_name='references'

urlpatterns = [
    path('', views.ReferencesListView.as_view(), name='api_views_list'),
    path('view/', views.ReferencesListView.as_view(), name='api_views_list'),
    path('view/<int:pk>/', views.ReferencesDetailView.as_view(), name='api_views_detail'),
]