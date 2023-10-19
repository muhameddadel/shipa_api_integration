from django.contrib import admin
from django.urls import path, include
from .connection import ShipaDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('shipa_data/', ShipaDataView.as_view(), name='shipa_data'),
    path('', include('teqneia.urls'))
]
