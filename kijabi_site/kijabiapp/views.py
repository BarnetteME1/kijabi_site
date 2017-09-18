from django.shortcuts import render, render_to_response
# Create your views here.

def data_input(request):
    return render_to_response(template_name="data-input.html")

def query(request):
    return render_to_response(template_name="query.html")

def analytics(request):
    return render_to_response(template_name="analytics.html")
