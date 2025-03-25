from django.contrib import admin
from .models import college, programs, organization, students, organizationmember
# Register your models here.
admin.site.register(college)
admin.site.register(programs)
admin.site.register(organization)
admin.site.register(students)
admin.site.register(organizationmember)