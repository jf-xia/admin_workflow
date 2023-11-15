'''
Add the code for entity-attribute-value model here.
This is a simple model that allows us to store data in a generic way.
We can store any type of data in this model, the model has 3 table: Entity, Value, and Relation. 
Entity has code, name, type, parent_id, is_enabled, description, owner, belong_to (json [entity_id...]), has_many (json [entity_id...]), attribute (json [{"code":"","label":"","frontend":"Component","setting":{},"default":"","list":"1","report":"1","is_filterable":"0","is_searchable":"0","is_required":"0","order":"","help":"","placeholder":"",}...]), created_at, updated_at, deleted_at.
Value has entity_id, entity_data (json {}), created_at, updated_at, deleted_at.
Relation has pk_entity_id, pk_value_id, fk_entity_id, fk_value_id.
'''
from django.db import models
from service.base_model import BaseModel


class Entity(BaseModel):
    code = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    parent_id = models.IntegerField(null=True)
    is_enabled = models.BooleanField(null=True)
    description = models.CharField(max_length=555, null=True)
    owner = models.IntegerField(null=True)
    belong_to = models.JSONField(null=True)
    has_many = models.JSONField(null=True)
    attribute = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Value(BaseModel):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    entity_data = models.JSONField(null=True)
    user_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # push Value.id in to entity_data  when get entity_data
    @property
    def get_entity_data(self):
        entity_data = self.entity_data
        entity_data = {'id': self.id, **entity_data}
        return entity_data


class Relation(BaseModel):
    pk_entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, related_name='pk_entity')
    pk_value = models.ForeignKey(
        Value, on_delete=models.CASCADE, related_name='pk_value')
    fk_entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, related_name='fk_entity')
    fk_value = models.ForeignKey(
        Value, on_delete=models.CASCADE, related_name='fk_value')
