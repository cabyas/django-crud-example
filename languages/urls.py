from django.urls import path

from languages import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('language/<int:pk>/', views.LanguageDetailView.as_view(), name='language_detail'),
    path('language/create/', views.LanguageCreateView.as_view(), name='language_create'),
    path('language/update/<int:pk>/', views.LanguageUpdateView.as_view(), name='language_update'),
    path('language/delete/<int:pk>/', views.LanguageDeleteView.as_view(), name='language_delete')
]