from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import API_objects
from .views import API_objects_details

urlpatterns=[
    path('basic/',API_objects.as_view()),
    path('basic/<int:pk>',API_objects_details.as_view())
]


urlpatterns=format_suffix_patterns(urlpatterns)
