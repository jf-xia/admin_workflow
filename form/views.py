from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.forms.models import model_to_dict

from service.format_response import api_response
from .models import Entity, Value, Relation


def entity_list(request):
    if request.method == 'GET':
        entities = Entity.objects.all()
        return api_response(data=[model_to_dict(entity) for entity in entities])
    elif request.method == 'POST':
        entity_data = request.POST
        entity = Entity.objects.create(**entity_data)
        return api_response(data=model_to_dict(entity), status=201)


def entity_detail(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    if request.method == 'GET':
        return api_response(data=model_to_dict(entity))
    elif request.method == 'PUT':
        entity_data = request.POST
        for key, value in entity_data.items():
            setattr(entity, key, value)
        entity.save()
        return api_response(data=model_to_dict(entity))
    elif request.method == 'DELETE':
        entity.delete()
        return api_response(status=204)


def value_list(request):
    if request.method == 'GET':
        values = Value.objects.all()
        paginator = Paginator(values, 10)  # Show 10 values per page
        page = request.GET.get('page')
        values = paginator.get_page(page)
        return api_response(data=[value.get_dict() for value in values])
    elif request.method == 'POST':
        value_data = request.POST
        value = Value.objects.create(**value_data)
        return api_response(data=value.get_dict(), status=201)


def value_detail(request, value_id):
    value = get_object_or_404(Value, pk=value_id)
    if request.method == 'GET':
        return api_response(data=value.get_dict())
    elif request.method == 'PUT':
        value_data = request.POST
        for key, val in value_data.items():
            setattr(value, key, val)
        value.save()
        return api_response(data=value.get_dict())
    elif request.method == 'DELETE':
        value.delete()
        return api_response(status=204)


def relation_list(request):
    if request.method == 'GET':
        relations = Relation.objects.all()
        paginator = Paginator(relations, 10)  # Show 10 relations per page
        page = request.GET.get('page')
        relations = paginator.get_page(page)
        return api_response(data=[relation.get_dict() for relation in relations])
    elif request.method == 'POST':
        relation_data = request.POST
        relation = Relation.objects.create(**relation_data)
        return api_response(data=relation.get_dict(), status=201)


def relation_detail(request, relation_id):
    relation = get_object_or_404(Relation, pk=relation_id)
    if request.method == 'GET':
        return api_response(data=relation.get_dict())
    elif request.method == 'PUT':
        relation_data = request.POST
        for key, val in relation_data.items():
            setattr(relation, key, val)
        relation.save()
        return api_response(data=relation.get_dict())
    elif request.method == 'DELETE':
        relation.delete()
        return api_response(status=204)
