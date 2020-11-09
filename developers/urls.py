from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_developers, name='developers'),
    path('<developer_id>', views.developer_detail, name='developer_detail'),
]