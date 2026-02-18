from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from .models import Organization, Student, OrgMember, Program
from .forms import SearchForm


class HomePageView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = "home.html"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(short_name__icontains=q))
        return qs.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET or None)
        context['form'] = form
        # summary counts for dashboard
        context['organization_count'] = Organization.objects.count()
        context['student_count'] = Student.objects.count()
        context['member_count'] = OrgMember.objects.count()
        context['program_count'] = Program.objects.count()
        return context
