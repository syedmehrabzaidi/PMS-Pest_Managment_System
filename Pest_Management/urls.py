from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='home page'),
    path('page2.html', views.second ,name='page'),
    path('add.html', views.add ,name='addpage'),
    path('form1', views.form_add ,name='formpage'),
    path('delete/<int:id>/', views.delete_data ,name='datadelete'),


]