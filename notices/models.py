from django.db import models
from django.utils import timezone

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, null=True)  # Allow null values
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name or 'Department'  # Handle potential null name

class Drive(models.Model):

    DRIVE_STATUS_CHOICES = [
        ('Closed', 'Closed'),
        ('Active', 'Active'),
        ('Upcoming', 'Upcoming'),
    ]

    Reference_no = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=30, null=True)
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    date = models.DateField(null=True)
    application_last_date = models.DateField(default='2002-12-02', null=True)
    content = models.TextField(null=True)
    Bond = models.CharField(max_length=50, null=True)
    industry_type = models.CharField(max_length=50, null=True)
    department = models.ManyToManyField(Department)
    job_role = models.CharField(max_length=50, null=True)
    job_location = models.CharField(max_length=50, null=True)
    job_eligibility = models.TextField(null=True)
    job_description = models.TextField(null=True)
    job_CTC = models.CharField(max_length=50, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    drive_id = models.AutoField(primary_key=True)
    application_link = models.CharField(max_length=100, null=True, blank=True)
    resume_link = models.CharField(max_length=200, blank=True, null=True)
    num_rounds = models.IntegerField(default=1, verbose_name='Number of Rounds', null=True)
    round1 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Round 1 Name', default='Round 1')
    round2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Round 2 Name')
    round3 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Round 3 Name')
    round4 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Round 4 Name')
    round5 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Round 5 Name')
    drive_status = models.CharField(max_length=10, choices=DRIVE_STATUS_CHOICES, default='Upcoming', null=True)

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        if self.date == today:
            self.drive_status = 'Active'
        elif self.date > today:
            self.drive_status = 'Upcoming'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'Drive'  # Handle potential null title

class Activity(models.Model):

    ACTIVITY_STATUS_CHOICES = [
        ('Closed', 'Closed'),
        ('Active', 'Active'),
        ('Upcoming', 'Upcoming'),
    ]

    Reference_no = models.CharField(max_length=100, null=True)
    activity_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True)
    industry_type = models.CharField(max_length=255, null=True)
    activity_date = models.DateField(null=True)
    department = models.ManyToManyField(Department)
    content = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    activity_status = models.CharField(max_length=10, choices=ACTIVITY_STATUS_CHOICES, default='Upcoming', null=True)

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        if self.activity_date == today:
            self.activity_status = 'Active'
        elif self.activity_date > today:
            self.activity_status = 'Upcoming'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'Activity'  # Handle potential null title

class Booklets(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    booklet = models.FileField(upload_to='booklets/', null=True)  # Allow null values
    department = models.ManyToManyField(Department)
    company_name = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.company_name or 'Booklet'  # Handle potential null name