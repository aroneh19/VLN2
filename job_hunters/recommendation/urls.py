from django.urls import path
from .views import (
    get_recommendation,
    create_recommendation,
    update_recommendation,
    delete_recommendation
)

urlpatterns = [
    path('recommendations/<int:recom_id>/', get_recommendation, name='get_recommendation'),
    path('recommendations/', create_recommendation, name='create_recommendation'),
    path('recommendations/<int:recom_id>/', update_recommendation, name='update_recommendation'),
    path('recommendations/<int:recom_id>/', delete_recommendation, name='delete_recommendation'),
]