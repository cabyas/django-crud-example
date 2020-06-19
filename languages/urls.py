from django.urls import path, include

from languages import views
from languages import views_fbv

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('language/<int:pk>/', views.LanguageDetailView.as_view(), name='language_detail'),
    path('language/create/', views.LanguageCreateView.as_view(), name='language_create'),
    path('language/update/<int:pk>/', views.LanguageUpdateView.as_view(), name='language_update'),
    path('language/delete/<int:pk>/', views.LanguageDeleteView.as_view(), name='language_delete'),

    path('fbv/', include([
        path('', views_fbv.home_view, name='fbv_home'),
        path('language/<int:pk>/', views_fbv.language_details_view, name='fbv_language_detail'),
        path('language/create/', views_fbv.language_create_view, name='fbv_language_create'),
        path('language/update/<int:pk>/', views_fbv.language_update_view, name='fbv_language_update'),
        path('language/delete/<int:pk>/', views_fbv.language_delete_view, name='fbv_language_delete'),
    ]))
]