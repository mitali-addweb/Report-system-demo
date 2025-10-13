from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles_or_permissions

"""
@allowed_roles_or_permissions(roles=['MDI Team'])
@allowed_roles_or_permissions(permissions=['reports.add_report'])
@allowed_roles_or_permissions(roles=['MDI Team'], permissions=['reports.add_report'])

"""

@login_required
def dashboard(request):
    user = request.user
    if user.groups.filter(name="MDI Team").exists():
        return redirect('mdi_dashboard')
    elif user.groups.filter(name="Client").exists():
        return redirect('client_dashboard')
    else:
        return redirect('access_denied')

@login_required
@allowed_roles_or_permissions(roles=['MDI Team'])
def mdi_dashboard(request):
    return render(request, 'mdi_dashboard.html')

@login_required
@allowed_roles_or_permissions(roles=['Client'])
def client_dashboard(request):
    return render(request, 'client_dashboard.html')

def access_denied(request):
    return render(request, 'access_denied.html')
