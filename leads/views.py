from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm
from django.views.generic import (
    TemplateView,
    ListView,
)

#####
class LandingPageView(TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, 'landing.html')
#####

#####
class LeadListView(ListView):
    model = Lead
    context_object_name = 'leads'
    template_name = 'leads/leads_list.html'

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }
    return render(request, 'leads/leads_list.html', context)
#####

#####
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {'lead': lead}
    return render(request, 'leads/leads_details.html', context)


"""
def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)
"""

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leads:leads_list")
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:leads_details', pk=lead.id)
    context = {
        "form": form,
        "lead": lead,
    }
    return render(request, 'leads/leads_update.html', context)


def lead_delete(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    lead.delete()
    return redirect('leads:leads_list')



