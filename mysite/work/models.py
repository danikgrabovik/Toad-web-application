from django.db import models

class Work(models.Model):
    type_of_work = models.CharField(max_length=30)
    reward_score = models.IntegerField()
    reward_money = models.IntegerField()

    def __str__(self):
        return self.type_of_work

# Create your models here.
