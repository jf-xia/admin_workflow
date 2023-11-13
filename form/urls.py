from django.urls import path
from . import views

urlpatterns = [
    path('entities/', views.entity_list, name='entity_list'),
    path('entities/<int:entity_id>/', views.entity_detail, name='entity_detail'),
    path('values/', views.value_list, name='value_list'),
    path('values/<int:value_id>/', views.value_detail, name='value_detail'),
    path('relations/', views.relation_list, name='relation_list'),
    path('relations/<int:relation_id>/',
         views.relation_detail, name='relation_detail'),
]
