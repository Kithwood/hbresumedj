from django.contrib import admin

# Register your models here.
from .models import Resume, EmploymentInfo, Accomplishment, Skill

admin.site.register(Resume)
admin.site.register(EmploymentInfo)
admin.site.register(Accomplishment)
admin.site.register(Skill)
