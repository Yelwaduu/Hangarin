from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
     id = models.CharField(max_length=20, primary_key=True)
     name = models.CharField(max_length=150)

     def __str__(self):
         return self.name
     
     class Meta:
          verbose_name = 'Priority'
          verbose_name_plural = 'Priorities'

class Category(BaseModel):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
              verbose_name = 'Category'
              verbose_name_plural = 'Categories'

class Task(BaseModel):
    id = models.CharField(max_length=20, primary_key=True) 
    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=60, choices=[('Pending', 'Pending'), 
                             ('In Progress','In Progress'),
                             ('Completed','Completed')], default='pending')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
            return self.title

class Note(BaseModel):
     id = models.CharField(max_length=20, primary_key=True)
     task = models.ForeignKey(Task, on_delete=models.CASCADE)
     content = models.TextField()

     def __str__(self):
          return str(self.task)

class SubTask(BaseModel):
     id = models.CharField(max_length=20, primary_key=True)
     parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
     title = models.CharField(max_length=150)
     status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress','In Progress'),
                                                       ('Completed', 'Completed')], default='pending')
     def __str__(self):
          return self.title




