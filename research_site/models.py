from django.db import models
from jsonfield import JSONField


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True)

    class Meta:
        unique_together = (('name', 'age', 'grade', 'phone'),)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    font_answer = JSONField(default=dict)
