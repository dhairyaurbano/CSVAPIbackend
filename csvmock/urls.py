from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView, PONumberView, TemplateView, SystemView, UserView, GroupView, TaskStatusView, TaskView, TimeLogView, TimeLogFilteredView

# Swagger Imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Router
router = DefaultRouter()
router.register(r"company", CompanyView, basename="company")
router.register(r'ponumbers', PONumberView, basename='ponumber')
router.register(r'templates', TemplateView, basename='template')
router.register(r'systems', SystemView, basename='system')
router.register(r'users', UserView, basename='user')
router.register(r'groups', GroupView, basename='group')
router.register(r'taskstatus', TaskStatusView, basename='taskstatus')
router.register(r'tasks', TaskView, basename='task')
router.register(r'timelogs', TimeLogView, basename='timelog')
router.register(r'timelogsfiltered', TimeLogFilteredView, basename='timelogfiltered')

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="CSVMock API",
        default_version="v1",
        description="Test API for company list",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),  # Your API endpoints
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
