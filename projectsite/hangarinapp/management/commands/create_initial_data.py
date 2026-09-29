from django.core.management import BaseCommand
from faker import Faker
from hangarinapp.models import SubTask, Note, Task, Category, Priority
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self,*args, **kwargs):
            self.create_task(10)
            self.create_subtask(10)
            self.create_note(10)


    def create_subtask(self, count):
        fake = Faker() 
        taskobj = list(Task.objects.all())

        for _ in range(count):
            SubTask.objects.create(
                id = str(fake.unique.random_number(digits=10)),
                parent_task = fake.random_element(elements=taskobj),
                title = fake.sentence(nb_words=5),
                status = fake.random_element(elements=['Pending','In Progress','Completed'])
            )
        
        self.stdout.write(
             self.style.SUCCESS(
                  "Initial data for Subtask created sucessfully"
             )
        )

    def create_task(self , count):
         
         categoryobj = list(Category.objects.all())
         priorityobj = list(Priority.objects.all())
         fake = Faker()
         for _ in range(count):
              
              Task.objects.create(
                   id = str(fake.unique.random_number(digits=10)),
                   title = fake.sentence(nb_words=5),
                   description= fake.paragraph(nb_sentences=3),
                   deadline = timezone.make_aware(fake.date_time_this_month()),
                    status = fake.random_element(elements=['Pending', 'In Progress', 'Completed']),
                   category = fake.random_element(elements=categoryobj),
                   priority = fake.random_element(elements=priorityobj)
                )

         self.stdout.write(
              self.style.SUCCESS(
                   'Initial data for Task created successfully '
              )
         )

    def create_note(self, count):
         fake = Faker()
         taskobj = list(Task.objects.all())

         for _ in range (count):
              
          Note.objects.create(
              id = str(fake.unique.random_number(digits=10)),
              task = fake.random_element(elements=taskobj),
              content = fake.paragraph(nb_sentences=3),

         )
     
         self.stdout.write(
             self.style.SUCCESS(
                  'Initial data for Note successfully created'
             )
        )