"""
URL configuration for ReportSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'report'

urlpatterns = [
    # Report
    path('create_report/', views.create_report, name='create_report'),
    path('display_report/', views.display_report, name='display_report'),
    path('report/<int:report_id>/', views.view_report, name='view_report'),
    path('update/<int:report_id>/', views.update_report, name='update_report'),
    path('report/<int:report_id>/export/', views.export_report_pdf, name='export_report_pdf'),
    path('report/<int:report_id>/export-word/', views.export_report_word, name='export_report_word'),
    path('report/<int:report_id>/export-csv/', views.export_report_csv, name='export_report_csv'),
    path('report/import/', views.import_report_csv, name='import_report'),

    # Asset
    path('create_asset/', views.create_asset, name='create_asset'),
    path('assets/', views.display_assets, name='display_assets'),
    path('assets/<int:asset_id>/', views.view_asset, name='view_asset'),
    path('assets/update/<int:asset_id>/', views.update_asset, name='update_asset'),

    # Problem Type
    path('create_problem_type/', views.create_problem_type, name='create_problem_type'),
    path('problem_type/', views.display_problem_type, name='display_problem_type'),
    path('problem_type/update/<int:problem_type_id>/', views.update_problem_type, name='update_problem_type'),


    path('assets1/update-parent/', views.update_asset_parent, name='update_asset_parent'),

]
