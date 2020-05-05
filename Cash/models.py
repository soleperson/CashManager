from django.db import models


# Create your models here.
class Cash(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_time = models.DateField()
    investment = models.FloatField(default=0.0000)
    share = models.FloatField(default=0.0000)
    worth = models.FloatField(default=0.0000)
    fee = models.FloatField(default=0.00)

    def __str__(self):
        return f"<{self.created_time}:{self.share}>"
