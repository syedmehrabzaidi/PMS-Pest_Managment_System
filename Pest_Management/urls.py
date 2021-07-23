from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='homepage'),
    path('page2.html', views.second ,name='page'),
    path('add.html', views.add ,name='addpage'),
    path('form1', views.form_add ,name='formpage'),
    path('delete/<int:id>/', views.delete_data ,name='datadelete'),
    #path('<int:id>/', views.update_data ,name='dataupdate'),
    path('<int:id>/', views.updatedmethod ,name='updated'),

]