from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.decorators import action
import random

graph_data_variations = {
            1: [
                {"id": 12, "name": "Hemanshi Kambaliya", "todo": random.randint(0, 10), "inProgress": random.randint(0, 5), "completed": random.randint(10, 20)},
                {"id": 14, "name": "Karan Patel", "todo": random.randint(10, 70), "inProgress": random.randint(0, 10), "completed": random.randint(10, 30)},
                {"id": 15, "name": "Anil Kumar", "todo": random.randint(5, 20), "inProgress": random.randint(0, 3), "completed": random.randint(5, 15)},
                {"id": 16, "name": "Priya Sharma", "todo": random.randint(0, 5), "inProgress": random.randint(2, 6), "completed": random.randint(10, 18)},
                {"id": 17, "name": "Rahul Verma", "todo": random.randint(20, 40), "inProgress": random.randint(0, 5), "completed": random.randint(8, 12)}
            ],
            2: [
                {"id": 18, "name": "Alisha Singh", "todo": random.randint(0, 20), "inProgress": random.randint(0, 5), "completed": random.randint(5, 12)},
                {"id": 19, "name": "Jignesh Patel", "todo": random.randint(10, 60), "inProgress": random.randint(2, 8), "completed": random.randint(12, 22)},
                {"id": 20, "name": "Maya Iyer", "todo": random.randint(3, 15), "inProgress": random.randint(1, 4), "completed": random.randint(7, 16)},
                {"id": 21, "name": "Deepak Mehta", "todo": random.randint(0, 10), "inProgress": random.randint(0, 6), "completed": random.randint(15, 25)},
                {"id": 22, "name": "Sonia Singh", "todo": random.randint(5, 30), "inProgress": random.randint(0, 4), "completed": random.randint(10, 20)}
            ],
            3: [
                {"id": 23, "name": "Vishal Agarwal", "todo": random.randint(0, 50), "inProgress": random.randint(1, 7), "completed": random.randint(10, 20)},
                {"id": 24, "name": "Neha Rathi", "todo": random.randint(15, 45), "inProgress": random.randint(0, 6), "completed": random.randint(5, 15)},
                {"id": 25, "name": "Amit Joshi", "todo": random.randint(0, 10), "inProgress": random.randint(2, 4), "completed": random.randint(12, 18)},
                {"id": 26, "name": "Ravi Soni", "todo": random.randint(5, 35), "inProgress": random.randint(0, 3), "completed": random.randint(8, 16)},
                {"id": 27, "name": "Manju Patil", "todo": random.randint(0, 20), "inProgress": random.randint(1, 5), "completed": random.randint(5, 12)}
            ],
            4: [
                {"id": 28, "name": "Ashok Kumar", "todo": random.randint(0, 30), "inProgress": random.randint(2, 5), "completed": random.randint(8, 18)},
                {"id": 29, "name": "Kritika Gupta", "todo": random.randint(10, 50), "inProgress": random.randint(0, 4), "completed": random.randint(15, 25)},
                {"id": 30, "name": "Harshit Mehta", "todo": random.randint(0, 20), "inProgress": random.randint(3, 8), "completed": random.randint(7, 18)},
                {"id": 31, "name": "Simran Kaur", "todo": random.randint(10, 40), "inProgress": random.randint(0, 6), "completed": random.randint(5, 13)},
                {"id": 32, "name": "Sandeep Yadav", "todo": random.randint(5, 30), "inProgress": random.randint(1, 4), "completed": random.randint(12, 22)}
            ]
        }

# In-memory storage for example (replace with DB later)

ponumberlist=[ {
        "id": 27,
        "po_number": "Test PO 001",
        "estimated_hours": 12232323,
        "actual_hours_spend": 0,
        "companyname": "Amazon",
        "company_location": "Jaipur"
      },
      {
        "id": 28,
        "po_number": "Test PO 002 changed2",
        "estimated_hours": 100223,
        "actual_hours_spend": 0,
        "companyname": "Amazon",
        "company_location": "Jaipur"
      },
      {
        "id": 29,
        "po_number": "Test PO 002 changed15",
        "estimated_hours": 1002,
        "actual_hours_spend": 0,
        "companyname": "Amazon",
        "company_location": "Banglore245"
      },
      {
        "id": 30,
        "po_number": "fish po number",
        "estimated_hours": 23,
        "actual_hours_spend": 0,
        "companyname": "Amazon",
        "company_location": "Jaipur"
      },
      {
        "id": 31,
        "po_number": "dog poC1D1E1",
        "estimated_hours": 34,
        "actual_hours_spend": 0,
        "companyname": "Amazon",
        "company_location": "Jaipur"
      }]
companieslist = [
     {
        "id": 1,
        "name": "Flipkart",
        "website": "https://www.flipkart.com/"
      },
      {
        "id": 2,
        "name": "Amazon",
        "website": "https://www.amazon.com"
      },
      {
        "id": 3,
        "name": "Netflix",
        "website": "http://netflix.com"
      },
      {
        "id": 4,
        "name": "new go",
        "website": "https://alibaba.com"
      },
      {
        "id": 46,
        "name": "Baba company",
        "website": "https://google.com"
      },
      {
        "id": 54,
        "name": "Baba elichidd 2sdsdsds",
        "website": "https://google.com"
      }
]

templateslist = [
    {
        "id": 23,
        "tasks": [
            {
                "id": 42,
                "statuses": [
                    {
                        "id": 69,
                        "unique_id": "6b7ff671-3878-4b35-af36-8689a5c602ef",
                        "created_at": "2025-04-11T16:27:16.820756+05:30",
                        "updated_at": "2025-04-11T16:27:16.820772+05:30",
                        "state": "applicable",
                        "status_name": "Status 1",
                        "task": 42,
                        "dependent_statuses": []
                    }
                ],
                "unique_id": "60a44b31-6cbb-4811-96a9-23e07066dd7b",
                "created_at": "2025-04-11T16:27:16.817870+05:30",
                "updated_at": "2025-04-11T16:27:16.817887+05:30",
                "title": "Template Task 1",
                "description": "this is the sample description",
                "template": 23
            }
        ],
        "unique_id": "cb3ea84a-8161-4183-9571-724f0f9e6202",
        "created_at": "2025-04-11T16:27:16.809793+05:30",
        "updated_at": "2025-04-11T16:27:16.809811+05:30",
        "title": "Custom Template",
        "description": "this is custom template description"
    },
    {
        "id": 22,
        "tasks": [
            {
                "id": 41,
                "statuses": [
                    {
                        "id": 68,
                        "unique_id": "f44e1f10-612f-41ee-bca9-3728166ba13b",
                        "created_at": "2025-03-21T18:27:08.304090+05:30",
                        "updated_at": "2025-03-21T18:27:08.304096+05:30",
                        "state": "applicable",
                        "status_name": "Status 1",
                        "task": 41,
                        "dependent_statuses": []
                    }
                ],
                "unique_id": "b2980dfe-26ea-4cd6-a364-81ba10c21087",
                "created_at": "2025-03-21T18:27:08.303426+05:30",
                "updated_at": "2025-03-21T18:27:08.303433+05:30",
                "title": "Task 1",
                "description": "Default description",
                "template": 22
            }
        ],
        "unique_id": "7ddefb86-c55b-4572-918e-ff2a9d1d5a6b",
        "created_at": "2025-03-21T18:27:08.302510+05:30",
        "updated_at": "2025-03-21T18:27:08.302523+05:30",
        "title": "Last template",
        "description": "sdsddsd"
    },
    {
        "id": 21,
        "tasks": [
            {
                "id": 40,
                "statuses": [
                    {
                        "id": 67,
                        "unique_id": "c222d833-eea9-481d-b2f0-a65faeb20a48",
                        "created_at": "2025-03-21T18:26:52.905380+05:30",
                        "updated_at": "2025-03-21T18:26:52.905386+05:30",
                        "state": "not applicable",
                        "status_name": "Status 1",
                        "task": 40,
                        "dependent_statuses": []
                    }
                ],
                "unique_id": "c873843e-bd45-4af8-b270-6bbc9c5868f7",
                "created_at": "2025-03-21T18:26:52.904829+05:30",
                "updated_at": "2025-03-21T18:26:52.904835+05:30",
                "title": "Task 1",
                "description": "Default description",
                "template": 21
            }
        ],
        "unique_id": "722b8898-b18d-4a4a-a7b6-dbc2fd5ef08d",
        "created_at": "2025-03-21T18:26:52.903823+05:30",
        "updated_at": "2025-03-21T18:26:52.903837+05:30",
        "title": "hhhhhhhhhh",
        "description": "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    },
    {
        "id": 20,
        "tasks": [
            {
                "id": 39,
                "statuses": [
                    {
                        "id": 66,
                        "unique_id": "2907d186-4588-44ef-80dc-09215a050dbd",
                        "created_at": "2025-03-21T18:26:48.864098+05:30",
                        "updated_at": "2025-03-21T18:26:48.864104+05:30",
                        "state": "applicable",
                        "status_name": "Status 1",
                        "task": 39,
                        "dependent_statuses": []
                    }
                ],
                "unique_id": "f0be2880-113c-4068-bb96-88136d6a33bc",
                "created_at": "2025-03-21T18:26:48.863527+05:30",
                "updated_at": "2025-03-21T18:26:48.863532+05:30",
                "title": "Task 1",
                "description": "Default description",
                "template": 20
            }
        ],
        "unique_id": "c61f4a32-f0ee-4404-a026-0a3c0865089b",
        "created_at": "2025-03-21T18:26:48.862760+05:30",
        "updated_at": "2025-03-21T18:26:48.862771+05:30",
        "title": "hhhhhhhhhh",
        "description": "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    }
]

systemlist = [
    {
        "id": 1,
        "systemid": "23",
        "systemname": "Custom statem",
        "status": "inprogress",
        "actual_spent_hours": 33.25,
        "company": "Flipkart"
    },
    {
        "id": 2,
        "systemid": "wewewewewew",
        "systemname": "fgfgfwew",
        "status": "todo",
        "actual_spent_hours": 0,
        "company": "Amazon"
    },
    {
        "id": 3,
        "systemid": "custom system id",
        "systemname": "custom system name",
        "status": "todo",
        "actual_spent_hours": 0,
        "company": "Amazon"
    },
    {
        "id": 4,
        "systemid": "Fish System id",
        "systemname": "Fish system name",
        "status": "todo",
        "actual_spent_hours": 0,
        "company": "Flipkart"
    }
]

userlist = [
    {
        "id": 1,
        "user": "AnonymousUser",
        "is_active": True,
        "is_staff": True,
        "is_superuser": True,
        "role": [
            "Software Engineer",
            "Engineer",
            "Group 2",
            "grop 3",
            "Group 4",
            "Group 5",
            "Group 565656",
            "saddsds",
            "sdsdsdsdsd",
            "Admin"
        ]
    }
]

grouplist = [
    {
        "id": 1,
        "group": "Admin"
    },
    {
        "id": 2,
        "group": "Software Engineer"
    },
    {
        "id": 3,
        "group": "Engineer"
    },
    {
        "id": 4,
        "group": "Group 2"
    },
    {
        "id": 5,
        "group": "grop 3"
    },
    {
        "id": 6,
        "group": "Group 4"
    }
]

taskstatuslist = [
    {
        "id": 23,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "no",
        "system": "custom system id-custom system name"
    },
    {
        "id": 24,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "no",
        "system": "Fish System id-Fish system name"
    },
    {
        "id": 25,
        "task": "Task 1",
        "status_name": "Status 3",
        "state": "no",
        "system": "Fish System id-Fish system name"
    },
    {
        "id": 26,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "no",
        "system": "dog system id-dog system name"
    },
    {
        "id": 27,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "no",
        "system": "ganesh  system id hai-ganesh system name hai"
    },
    {
        "id": 28,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "no",
        "system": "ererererere-erxcre"
    },
    {
        "id": 29,
        "task": "Task 1",
        "status_name": "Status 1",
        "state": "yes",
        "system": "wewewewe-wewewew"
    },
    {
        "id": 30,
        "task": "Payment in backend",
        "status_name": "Is Paytm payment integration Done?",
        "state": "yes",
        "system": "this is ecommerce id-Ecommerce"
    }
]

tasklist = [
    {
        "id": 23,
        "title": "Task 1",
        "description": None,
        "assigned_to": "testing@gmail.com",
        "actual_hours_spent": 0,
        "system": "custom system id-custom system name"
    },
    {
        "id": 24,
        "title": "Task 1",
        "description": None,
        "assigned_to": "AnonymousUser",
        "actual_hours_spent": 0,
        "system": "Fish System id-Fish system name"
    },
    {
        "id": 25,
        "title": "Task 1",
        "description": None,
        "assigned_to": "ajit",
        "actual_hours_spent": 0,
        "system": "dog system id-dog system name"
    }
]

timelogoriginallist = [
    {
        "id": 1,
        "task": "Server maintenance",
        "system_name": "Alpha",
        "system_id": "SYS-101",
        "date": "2025-03-15",
        "start_time": "09:00",
        "end_time": "12:00",
        "hours": 3,
        "added_by": "John",
        "po_number": "PO-4567"
    },
    {
        "id": 2,
        "task": "Software update",
        "system_name": "Beta",
        "system_id": "SYS-202",
        "date": "2025-03-16",
        "start_time": "13:00",
        "end_time": "17:00",
        "hours": 4,
        "added_by": "Alice",
        "po_number": "PO-5678"
    },
    {
        "id": 3,
        "task": "Data backup",
        "system_name": "Gamma",
        "system_id": "SYS-303",
        "date": "2025-03-17",
        "start_time": "08:30",
        "end_time": "11:30",
        "hours": 3,
        "added_by": "Mike",
        "po_number": "PO-6789"
    },
    {
        "id": 4,
        "task": "Security patch deployment",
        "system_name": "Delta",
        "system_id": "SYS-404",
        "date": "2025-03-18",
        "start_time": "22:00",
        "end_time": "02:00",
        "hours": 4,
        "added_by": "Sophia",
        "po_number": "PO-7890"
    },
    {
        "id": 5,
        "task": "Network optimization",
        "system_name": "Epsilon",
        "system_id": "SYS-505",
        "date": "2025-03-19",
        "start_time": "10:00",
        "end_time": "14:00",
        "hours": 4,
        "added_by": "David",
        "po_number": "PO-8901"
    },
    {
        "id": 6,
        "task": "Bug fix deployment",
        "system_name": "Zeta",
        "system_id": "SYS-606",
        "date": "2025-03-20",
        "start_time": "16:00",
        "end_time": "19:00",
        "hours": 3,
        "added_by": "Emma",
        "po_number": "PO-9012"
    },
    {
        "id": 7,
        "task": "Code review",
        "system_name": "Eta",
        "system_id": "SYS-707",
        "date": "2025-03-21",
        "start_time": "11:00",
        "end_time": "14:30",
        "hours": 3.5,
        "added_by": "James",
        "po_number": "PO-0123"
    },
    {
        "id": 8,
        "task": "Server reboot",
        "system_name": "Theta",
        "system_id": "SYS-808",
        "date": "2025-03-22",
        "start_time": "05:00",
        "end_time": "06:30",
        "hours": 1.5,
        "added_by": "Olivia",
        "po_number": "PO-1234"
    },
    {
        "id": 9,
        "task": "System health check",
        "system_name": "Iota",
        "system_id": "SYS-909",
        "date": "2025-03-23",
        "start_time": "07:00",
        "end_time": "09:30",
        "hours": 2.5,
        "added_by": "Ethan",
        "po_number": "PO-2345"
    },
    {
        "id": 10,
        "task": "Performance testing",
        "system_name": "Kappa",
        "system_id": "SYS-1010",
        "date": "2025-03-24",
        "start_time": "14:00",
        "end_time": "18:00",
        "hours": 4,
        "added_by": "Sophia",
        "po_number": "PO-3456"
    }
]

getSpecificTimelogdata={
     "id": 1,
        "task": "Server maintenance",
        "system_name": "Alpha",
        "system_id": "SYS-101",
        "date": "2025-03-15",
        "description": "Routine server maintenance and updates.",
        "start_time": "09:00",
        "end_time": "12:00",
        "hours": 3,
        "added_by": "John",
        "po_number": "PO-4567"
};


class TimeLogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    description = serializers.CharField()
    task = serializers.CharField()
    system_name = serializers.CharField()
    added_by = serializers.CharField()

class PONumberView(viewsets.ViewSet):
    @swagger_auto_schema(operation_description="List all filtered and after deletion po number list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "ponumber listed successfully",
            "results": {
                "data": ponumberlist[:5],  # Only return first 5 entries
                "page": 1,
                "count": 5
            },
            "errors": 0
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Delete po number by ID")
    def destroy(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "po number deleted succesfully",
            "results": []
        }, status=status.HTTP_200_OK)


class CompanyView(viewsets.ViewSet):
    """
    Company CRUD APIs
    """

    
    


    @swagger_auto_schema(operation_description="List all filtered and after deletion companies list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "companies listed succesfully",
            "results": {
                "data":companieslist,
                "page": 1,
                "count":6
            },
            "errors":0
        }, status=status.HTTP_200_OK)
    



    @swagger_auto_schema(operation_description="Create a new company")
    def create(self, request):
        return Response({
            "statusCode": 201,
            "message": "Company created succesfully",
            "results": companieslist
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_description="Retrieve company by ID")
    def retrieve(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Company retrieved succesfully",
            "results": companieslist
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update company by ID")
    def update(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Company updated succesfully",
            "results": companieslist
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Delete company by ID")
    def destroy(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Company deleted succesfully",
            "results": []
        }, status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['get'], url_path='systems')
    def systems(self, request, pk=None):
        # Simulate fixed system list
        systems = [
        { "id": 1, "label": "System 1" },
        { "id": 2, "label": "System 2" },
        { "id": 3, "label": "System 3" },
        { "id": 4, "label": "System 4" }
        ];
        return Response({
            "statusCode": 200,
            "message": f"Systems for company {pk} listed successfully",
            "results": systems
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Get graph data for a specific system")
    @action(detail=True, methods=['get'], url_path='system/(?P<systemid>[^/.]+)/graphdata')
    def graph_data(self, request, pk=None, systemid=None):
        systemid = self.kwargs.get('systemid')  # Correct way to fetch it
        # Generate dummy data for different system IDs
        graph_data_variations = {
            1: [
                {"id": 12, "name": "Hemanshi Kambaliya", "todo": random.randint(0, 10), "inProgress": random.randint(0, 5), "completed": random.randint(10, 20)},
                {"id": 14, "name": "Karan Patel", "todo": random.randint(10, 70), "inProgress": random.randint(0, 10), "completed": random.randint(10, 30)},
                {"id": 15, "name": "Anil Kumar", "todo": random.randint(5, 20), "inProgress": random.randint(0, 3), "completed": random.randint(5, 15)},
                {"id": 16, "name": "Priya Sharma", "todo": random.randint(0, 5), "inProgress": random.randint(2, 6), "completed": random.randint(10, 18)},
                {"id": 17, "name": "Rahul Verma", "todo": random.randint(20, 40), "inProgress": random.randint(0, 5), "completed": random.randint(8, 12)}
            ],
            2: [
                {"id": 18, "name": "Alisha Singh", "todo": random.randint(0, 20), "inProgress": random.randint(0, 5), "completed": random.randint(5, 12)},
                {"id": 19, "name": "Jignesh Patel", "todo": random.randint(10, 60), "inProgress": random.randint(2, 8), "completed": random.randint(12, 22)},
                {"id": 20, "name": "Maya Iyer", "todo": random.randint(3, 15), "inProgress": random.randint(1, 4), "completed": random.randint(7, 16)},
                {"id": 21, "name": "Deepak Mehta", "todo": random.randint(0, 10), "inProgress": random.randint(0, 6), "completed": random.randint(15, 25)},
                {"id": 22, "name": "Sonia Singh", "todo": random.randint(5, 30), "inProgress": random.randint(0, 4), "completed": random.randint(10, 20)}
            ],
            3: [
                {"id": 23, "name": "Vishal Agarwal", "todo": random.randint(0, 50), "inProgress": random.randint(1, 7), "completed": random.randint(10, 20)},
                {"id": 24, "name": "Neha Rathi", "todo": random.randint(15, 45), "inProgress": random.randint(0, 6), "completed": random.randint(5, 15)},
                {"id": 25, "name": "Amit Joshi", "todo": random.randint(0, 10), "inProgress": random.randint(2, 4), "completed": random.randint(12, 18)},
                {"id": 26, "name": "Ravi Soni", "todo": random.randint(5, 35), "inProgress": random.randint(0, 3), "completed": random.randint(8, 16)},
                {"id": 27, "name": "Manju Patil", "todo": random.randint(0, 20), "inProgress": random.randint(1, 5), "completed": random.randint(5, 12)}
            ],
            4: [
                {"id": 28, "name": "Ashok Kumar", "todo": random.randint(0, 30), "inProgress": random.randint(2, 5), "completed": random.randint(8, 18)},
                {"id": 29, "name": "Kritika Gupta", "todo": random.randint(10, 50), "inProgress": random.randint(0, 4), "completed": random.randint(15, 25)},
                {"id": 30, "name": "Harshit Mehta", "todo": random.randint(0, 20), "inProgress": random.randint(3, 8), "completed": random.randint(7, 18)},
                {"id": 31, "name": "Simran Kaur", "todo": random.randint(10, 40), "inProgress": random.randint(0, 6), "completed": random.randint(5, 13)},
                {"id": 32, "name": "Sandeep Yadav", "todo": random.randint(5, 30), "inProgress": random.randint(1, 4), "completed": random.randint(12, 22)}
            ]
        }

        # Get the corresponding data for the selected systemid
        data = graph_data_variations.get(int(systemid), [])

        return Response({
            "statusCode": 200,
            "message": f"Graph data for system {systemid} listed successfully",
            "results": {
                "data": data,
                "totalponumbers": random.randint(10, 15),
                "totalemployees": random.randint(40, 60),
                "totalsytems": random.randint(20, 30)
            }
        }, status=status.HTTP_200_OK)

class TemplateView(viewsets.ViewSet):
    """
    Template CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion templates list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "templates listed successfully",
            "results": {
                "data": templateslist,
                "page": 1,
                "count": 4
            },
            "errors": 0
        }, status=status.HTTP_200_OK)

class SystemView(viewsets.ViewSet):
    """
    System CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion systems list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "systems listed successfully",
            "results": {
                "data": systemlist,
                "page": 1,
                "count": 4
            },
            "errors": 0
        }, status=status.HTTP_200_OK)

class UserView(viewsets.ViewSet):
    """
    User CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion users list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "users listed successfully",
            "results": {
                "data": userlist,
                "page": 1,
                "count": 1
            },
            "errors": 0
        }, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(operation_description="Retrieve Users by ID")
    def retrieve(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Users retrieved succesfully",
            "results": userlist[0]
        }, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(operation_description="Update Users by ID")
    def update(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Users updated succesfully",
            "results": userlist[0]
        }, status=status.HTTP_200_OK)

class GroupView(viewsets.ViewSet):
    """
    Group CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion groups list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "groups listed successfully",
            "results": {
                "data": grouplist,
                "page": 1,
                "count": 6
            },
            "errors": 0
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Retrieve group by ID")
    def retrieve(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Group retrieved succesfully",
            "results": grouplist[0]
        }, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(operation_description="Update group by ID")
    def update(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Group updated succesfully",
            "results": grouplist[0]
        }, status=status.HTTP_200_OK)

class TaskStatusView(viewsets.ViewSet):
    """
    TaskStatus CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion task status list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "task status listed successfully",
            "results": {
                "data": taskstatuslist,
                "page": 1,
                "count": 8
            },
            "errors": 0
        }, status=status.HTTP_200_OK)

class TaskView(viewsets.ViewSet):
    """
    Task CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all filtered and after deletion tasks list")
    def list(self, request):
        return Response({
            "statusCode": 200,
            "message": "success",
            "results": {
                "data": tasklist,
                "page": 1,
                "count": 3
            },
            "errors": None
        }, status=status.HTTP_200_OK)

class TimeLogView(viewsets.ViewSet):
    """
    TimeLog CRUD APIs
    """
    @swagger_auto_schema(operation_description="List all time logs")
    def list(self, request):
        return Response({
            "status": "success",
            "count": 26,
            "result": timelogoriginallist
        }, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(operation_description="Retrieve timelog by ID")
    def retrieve(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Timelog retrieved succesfully",
            "results": getSpecificTimelogdata
        }, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(
        operation_description="Create a new timelog",
        request_body=TimeLogSerializer
    )
    def create(self, request):
        return Response({
            "statusCode": 201,
            "message": "Timelog created successfully",
            "results": request.data  # Echoing back submitted data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_description="Update timelog by ID",request_body=TimeLogSerializer)
    def update(self, request, pk=None):
        return Response({
            "statusCode": 200,
            "message": "Timelog updated succesfully",
            "results": timelogoriginallist[0]
        }, status=status.HTTP_200_OK)

class TimeLogFilteredView(viewsets.ViewSet):
    """
    TimeLog Filtered APIs
    """
    @swagger_auto_schema(operation_description="List filtered time logs (6 entries)")
    def list(self, request):
        return Response({
            "status": "success",
            "count": 6,
            "result": timelogoriginallist[:6]  # Only return first 6 entries
        }, status=status.HTTP_200_OK)




class CompanyLocationView(viewsets.ViewSet):
    """
    Company CRUD APIs
    """
    @swagger_auto_schema(operation_description="Delete company by ID", tags=["CompanyLocation"])
    def destroy(self, request, company_id,location_id):
        return Response({
            "statusCode": 200,
            "message": "Company loation deleted succesfully",
            "results": []
        }, status=status.HTTP_200_OK)
