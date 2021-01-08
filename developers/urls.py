from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_developers, name='developers'),
    path('<int:developer_id>/', views.developer_detail, name='developer_detail'),
    path('add/', views.add_developer, name='add_developer'),
    path('edit/<int:developer_id>/', views.edit_developer, name='edit_developer'),
]