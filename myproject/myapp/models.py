from django.db import models

# Create your models here.


class Course(models.Model):
    course = models.CharField(max_length=100 )

    def __str__(self):
        return self.course+'_'+str(self.id)


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course , on_delete=models.CASCADE )
    is_deleted = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


