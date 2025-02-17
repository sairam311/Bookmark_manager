from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls, name='urls'),
    path('update_url/<int:id>', views.update_url, name='update_url'),  # Added int:
    path('delete_url/<int:id>', views.delete_url, name='delete_url'),  # Added int:
    path('favorite_url/<int:id>', views.favorite_url, name='favorite_url'),  # Added int:
]
app_name = 'home'