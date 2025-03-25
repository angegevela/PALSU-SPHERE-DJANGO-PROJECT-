from django.core.management.base import BaseCommand
from faker import Faker
from projectsite.studentorg.models import college, programs, organization, student, organizationmember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_organization(self, count):
        fake = Faker()

        for _ in range(count):
            words = [fake.word() for _ in range(2)]  # two words
            organization_name = ' '.join(words)
            organization.objects.create(
                name=organization_name.title(),
                college=college.objects.order_by('?').first(),
                description=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for organization created successfully.'
        ))

    def create_students(self, count):
        fake = Faker()

        for _ in range(count):
            student.objects.create(
                student_id=f"{fake.random_int(2020, 2024)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=programs.objects.order_by('?').first()
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for students created successfully.'
        ))

    def create_membership(self, count):
        fake = Faker()

        for _ in range(count):
            organizationmember.objects.create(
                student=student.objects.order_by('?').first(),
                organization=organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for student organization created successfully.'
        ))
