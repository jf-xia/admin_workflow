from django.urls import path
from . import views

urlpatterns = [
    path('entity', views.entity_list, name='entity_list'),
    path('entity/<int:entity_id>', views.entity_detail, name='entity_detail'),
    path('e/<slug:entity_code>', views.value_list, name='value_list'),
    path('e/<slug:entity_code>/<int:value_id>',
         views.value_detail, name='value_detail'),
    path('relations', views.relation_list, name='relation_list'),
    path('relations/<int:relation_id>',
         views.relation_detail, name='relation_detail'),
]
