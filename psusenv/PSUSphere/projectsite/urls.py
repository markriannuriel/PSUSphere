"""
URL configuration for psuproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView,
    OrganizationList,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,
    CollegeList,
    CollegeCreateView,
    CollegeUpdateView,
    CollegeDeleteView,
    ProgramList,
    ProgramCreateView,
    ProgramUpdateView,
    ProgramDeleteView,
    StudentList,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    OrgMemberList,
    OrgMemberCreateView,
    OrgMemberUpdateView,
    OrgMemberDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organizations/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),

    # college urls
    path('colleges/', CollegeList.as_view(), name='college-list'),
    path('colleges/add', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),

    # program urls
    path('programs/', ProgramList.as_view(), name='program-list'),
    path('programs/add', ProgramCreateView.as_view(), name='program-add'),
    path('programs/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<int:pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),

    # student urls
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/add', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),

    # orgmember urls
    path('orgmembers/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmembers/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<int:pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
]
