from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:developer_id>/', views.add_review, name='add_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('', views.review_moderation, name='review_moderation'),
    path('review_approve/<int:review_id>/',
         views.approve_review, name='approve_review'),
    path('reject_review/<int:review_id>/',
         views.reject_review, name='reject_review'),
    path('dispute_review/<int:review_id>/',
         views.dispute_review, name='dispute_review'),
]
