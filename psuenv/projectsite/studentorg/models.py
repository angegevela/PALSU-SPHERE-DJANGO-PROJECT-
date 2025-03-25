from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class college(BaseModel):
    college_name = models.CharField(max_length=300)
    def __str__(self):
        return self.college_name

class programs(BaseModel):
    prog_names = models.CharField(max_length=300)
    def __str__(self):
        return self.prog_names
    
class organization(BaseModel):
    org_name = models.CharField(max_length=300)
    College = models.ForeignKey(college,null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.org_name
    

class students(BaseModel):
    student_id = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    programs = models.ForeignKey(programs, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.lastname},{self.firstname}"


class organizationmember(BaseModel):
    students = models.ForeignKey(students, on_delete=models.CASCADE)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    date_joined = models.DateField()
