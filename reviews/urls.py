from django.urls import path
from . import views

urlpatterns = [
    # path('', views.review, name='review'),
    path('add/<int:developer_id>/', views.add_review, name='add_review'),
    # path('edit/<int:developer_id>/', views.edit_review, name='edit_review'),
    # path('delete/<int:developer_id>/', views.delete_review, name='delete_review'),
]