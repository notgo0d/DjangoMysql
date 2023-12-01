from formsApp.views import home, manage_users, update_user, delete_user
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('manage/', manage_users, name='manage_users'),
    path('create/', manage_users, name='create_user'),
    path('update/<int:user_id>/', update_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]






