from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import forms, login
from django.views.generic import CreateView, UpdateView, View, TemplateView
from kijabiapp.models import Profile
# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/registration/login'

class DataView(TemplateView):
    model = Profile
    template_name="kijabi_app/data-input.html"

class QueryView(TemplateView):
    model = Profile
    template_name="kijabi_app/query.html"

class AnalyticsView(TemplateView):
    model = Profile
    template_name="kijabi_app/analytics.html"

#def data_input(request):
#    return render_to_response(template_name="kijabi_app/data-input.html")

#def query(request):
#    return render_to_response(template_name="kijabi_app/query.html")

#def analytics(request):
#    return render_to_response(template_name="kijabi_app/analytics.html")
