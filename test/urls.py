from django.urls import path
from .views import *

urlpatterns = [
    path('parcel/', CreateParcel.as_view(), name='create_parcel'),
    path('container/', CreateContainer.as_view(), name='create_container'),

    path('<str:container_number>/add_parcel_to_container/', AddParcelToContainer.as_view(), name='add_parcel_to_container'),
    path('<str:container_number>/close_container/', CloseContainer.as_view(), name='close_container'),
    path('<str:container_number>/add_trace_to_container/', AddTraceToContainer.as_view(), name='add_trace_to_container'),
    
    path('track_parcel/<str:parcel_number>/', TrackParcel.as_view(), name='parcel_number'),
    path('add_attachment_to_parcel/<str:schema>_<str:value>/', AddAttachementToParcel.as_view(), name='add_attachment_to_parcel'),
    path('parcel_label/<str:schema>_<str:value>/', GenerateParcelLabel.as_view(), name='parcel_label'),
    path('add_trace_to_parcel/', AddTraceToParcel.as_view(), name='parcel_number'),
]
