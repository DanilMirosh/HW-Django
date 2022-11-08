from django.contrib import admin
from django.urls import path

from ads import views
from ads.views import AdsView, AdView, CategoryView, CategoriesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cat/', CategoriesView.as_view()),
    path('ad/', AdsView.as_view()),
    path('cat/<int:pk>', CategoryView.as_view()),
    path('ad/<int:pk>', AdView.as_view()),
]