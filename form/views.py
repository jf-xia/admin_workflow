from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.forms.models import model_to_dict

from service.format_response import api_response
from .models import Entity, Value, Relation
import json

'''
rule: 
1. contract contract_start_date<payroll_date<contract_end_date
2. form each month only one charging_department 
3. what todo when employee_code is not exist in HRM system
4. has charging_department only got one charging_cost_centre
5. which role/department will maintain the project_code

create table payroll_request
(
    id                            bigint(10) unsigned auto_increment    primary key,
    employee_code                 bigint(10)                            not null,
    employee_category             enum ('Student', 'Staff')             not null,
    employee_mode                 enum ('FT', 'PT', '?Student?')        not null,
    payroll_date                  date                                  null,
    charging_department           entity                                null,
    charging_cost_centre          longtext                              null,
    project_code                  longtext                              null,
    submitted_by                  bigint(10) unsigned                   null,
    submitted_at                  datetime                              null,
    submitted_contact             varchar(128)                          null,
);

create table payroll_event
(
    id                 bigint(10) unsigned auto_increment           primary key,
    payroll_request_id bigint(10) unsigned                          not null,
    employee_id        bigint(10)                                   not null,
    event_id           bigint(10) unsigned                          null,
    event_name         varchar(128)                default ''       not null,
    date_from          date                                         null,
    date_to            date                                         null,
    num_of_hours       decimal(5, 1)                                null,
    payment_base       enum ('Hourly', 'Lump Sum') default 'Hourly' not null,
    payment_rate       decimal(5, 1)                                null,
    amount             decimal(5, 1)                                null,
    created_at         datetime                                     null,
    updated_at         datetime                                     null,
);

'''


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


def value_list(request, entity_code):
    if request.method == 'GET':
        entity_id = Entity.objects.get(code=entity_code).id or 0
        if (entity_id == 0):
            return HttpResponse(json.dumps({'error': 'entity_code not found'}), status=404)
        values = Value.objects.filter(entity=entity_id)
        paginator = Paginator(values, 10)  # Show 10 values per page
        page = request.GET.get('page') or 1
        values = paginator.get_page(page)
        return HttpResponse(json.dumps([value.get_entity_data for value in values]))
    elif request.method == 'POST':
        value_data = request.POST
        value = Value.objects.create(**value_data)
        return api_response(data=model_to_dict(value), status=201)


def value_detail(request, entity_code, value_id):
    value = get_object_or_404(Value, pk=value_id)
    if request.method == 'GET':
        return HttpResponse(json.dumps(value.get_entity_data))
    elif request.method == 'PATCH':
        return HttpResponse(json.dumps([1, 2]))
        value_data = request.POST
        for key, val in value_data.items():
            setattr(value, key, val)
        value.save()
        return HttpResponse(json.dumps(value.get_entity_data))
    elif request.method == 'DELETE':
        # value.delete()
        return HttpResponse(json.dumps(value.get_entity_data), status=204)


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
