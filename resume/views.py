from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Resume, EmploymentInfo, Accomplishment, Skill

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'resume/index.html'
    context_object_name = 'Resume'

    def get_queryset(self):
        """Return resume with id = 1."""
        return Resume.objects.filter(id=1)
