from django.db import models
class list (models.Model):
    item = models.CharField(max_length=300)
    when = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.completed)
