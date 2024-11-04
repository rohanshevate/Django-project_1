from django.db import models

# Create your models here.


class SubjectMarks(models.Model):
    student = models.Foreignkey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.Foreignkey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ["student", "subject"]
