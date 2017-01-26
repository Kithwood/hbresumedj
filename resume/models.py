from django.db import models

# Create your models here.
class Resume(models.Model):
    Name = models.CharField(max_length=56)
    Title = models.CharField(max_length=56)
    Summary = models.TextField()
    Location = models.CharField(max_length=200)
    Email = models.CharField(max_length=128)
    Phone = models.CharField(max_length=24)
    def __str__(self):
        return self.Name + "'s Resume"


class EmploymentInfo(models.Model):
    Resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    Title = models.CharField(max_length=56)
    Summary = models.TextField()
    Employer = models.CharField(max_length=128)
    From = models.DateField()
    To = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.Employer + " Info"



class Accomplishment(models.Model):
    EmploymentInfo = models.ForeignKey(EmploymentInfo, on_delete=models.CASCADE)
    Description = models.TextField()
    def __str__(self):
        return self.Description

class Skill(models.Model):
    Resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    SortOrder = models.IntegerField()
    Description = models.TextField()
    def __str__(self):
        return self.Description
