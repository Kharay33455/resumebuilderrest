from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 30)
    website = models.TextField()
    email = models.TextField()
    summary = models.TextField()
    job_role = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = "pfp")
    address = models.TextField()
    address_cont = models.TextField(blank = True, null = True)
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()

    def __str__(self):
        return f'Candidate {self.first_name} {self.last_name}'
    
class WorkExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    title = models.CharField(max_length = 59)
    company = models.CharField(max_length = 50)
    city= models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    date_start= models.DateField()
    date_end= models.DateField()
    is_current = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.title} for candidate {self.candidate}'

class KeyResponsibilities(models.Model):
    work_experience = models.ForeignKey(WorkExperience, on_delete = models.CASCADE)
    key_responsibilities = models.TextField()

class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length = 50)
    school_name = models.CharField(max_length = 50)
    start_date = models.DateField()
    graduation_date = models.DateField()
    grading = models.TextField(blank = True, null = True)

    def __str__(self):
        return f'{self.degree_name} from {self.school_name}'

class Skill(models.Model):
    name = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} for {self.candidate}'


class Language(models.Model):
    name = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} for {self.candidate}'

class Reference(models.Model):
    full_name = models.TextField()
    address = models.TextField()
    phone_number = models.CharField(max_length = 30)
    email = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)

    def __str__(self):
        return f'Reference {self.full_name} for {self.candidate}'

class Resume(models.Model):
	resumeID = models.CharField(max_length = 30)
	resume = models.FileField(upload_to = "resume")
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	job_role = models.CharField(max_length = 50)

	def __str__(self):
		return f"{self.first_name} {self.job_role} resume"

class Template(models.Model):
    name = models.CharField(max_length = 10)
    image = models.ImageField(upload_to="templates")

    def __str__(self):
        return self.name
