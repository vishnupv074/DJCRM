from django.urls import path
from .views import (lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateview, LeadDeleteView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='leads_details'),
    path('create/', LeadCreateView.as_view(), name='create_lead'),
    path('<int:pk>/update/', LeadUpdateview.as_view(), name='update_lead'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='delete_lead'),
]
