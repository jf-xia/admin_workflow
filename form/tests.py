import json
from django.test import TestCase, RequestFactory
from form.views import entity_list
from form.models import Entity


class EntityListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.entity_data = {
            'name': 'Test Entity',
            'description': 'This is a test entity'
        }

    def test_entity_list_GET(self):
        # Create some entities
        Entity.objects.create(id=1, code='request', name='Request', type=1, is_enabled=1,
                              description='Events of section to office', owner=1,
                              belong_to=[1], has_many=[], attribute=[
                                  {
                                      "code": "employee_code",
                                      "label": "Employee Code",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "employee_category",
                                      "label": "Employee Category",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "employee_mode",
                                      "label": "Employee Mode",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "payroll_date",
                                      "label": "Payroll Date",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "charging_department",
                                      "label": "Charging Department",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "charging_cost_centre",
                                      "label": "Charging Cost Centre",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "project_code",
                                      "label": "Project Code",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "submitted_by",
                                      "label": "Submitted By",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "submitted_at",
                                      "label": "Submitted At",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "submitted_contact",
                                      "label": "Submitted Contact",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  }
                              ]
                              )
        Value.objects.create(entity_id=1, entity_data={
            "employee_code": "H65489",
            "employee_category": "Staff",
            "employee_mode": "FT",
            "payroll_date": "2023-01-01",
            "charging_department": "SAO",
            "charging_cost_centre": "319",
            "project_code": "700004",
            "submitted_by": "1965",
            "submitted_at": "2023-01-01",
            "submitted_contact": "97030256"
        })
        Value.objects.create(entity_id=2, entity_data={
            "employee_code": "H65490",
            "employee_category": "Student",
            "employee_mode": "PT",
            "payroll_date": "2023-02-01",
            "charging_department": "HR",
            "charging_cost_centre": "320",
            "project_code": "700005",
            "submitted_by": "1966",
            "submitted_at": "2023-02-01",
            "submitted_contact": "97030257"
        })

        Entity.objects.create(id=2, code='payroll_event', name='Payroll Event', type=1, is_enabled=1,
                              description='Request Form of the section to office', owner=1,
                              belong_to=[], has_many=[2], attribute=[
                                  {
                                      "code": "payroll_request_id",
                                      "label": "Payroll Request ID",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "employee_id",
                                      "label": "Employee ID",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "event_id",
                                      "label": "Event ID",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "event_name",
                                      "label": "Event Name",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "date_from",
                                      "label": "Date From",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "date_to",
                                      "label": "Date To",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "num_of_hours",
                                      "label": "Number of Hours",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "payment_base",
                                      "label": "Payment Base",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "Hourly",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "1",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "payment_rate",
                                      "label": "Payment Rate",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "amount",
                                      "label": "Amount",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "created_at",
                                      "label": "Created At",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  },
                                  {
                                      "code": "updated_at",
                                      "label": "Updated At",
                                      "frontend": "Component",
                                      "setting": {},
                                      "default": "",
                                      "list": "1",
                                      "report": "1",
                                      "is_filterable": "0",
                                      "is_searchable": "0",
                                      "is_required": "0",
                                      "order": "",
                                      "help": "",
                                      "placeholder": ""
                                  }
                              ])
        # Make a GET request to the view
        request = self.factory.get('/entities/')
        response = entity_list(request)
        data = json.loads(response.content.decode('utf-8'))['data']
        # Check that the response contains the entities
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['code'], 'payroll_request')
        self.assertEqual(data[1]['code'], 'payroll_event')
