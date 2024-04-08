from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('data/', views.data, name='get_data'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete')
]
