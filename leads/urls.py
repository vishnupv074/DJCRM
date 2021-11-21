from django.urls import path
from .views import (lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView,
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', lead_detail, name='leads_details'),
    path('create/', lead_create, name='create_lead'),
    path('<int:pk>/update/', lead_update, name='update_lead'),
    path('<int:pk>/delete/', lead_delete, name='delete_lead'),
]
