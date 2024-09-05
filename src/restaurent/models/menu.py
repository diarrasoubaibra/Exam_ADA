from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from restaurent.models.plat import Plat

class Menu(DateTimeModel):
    plat = models.OneToOneField(Plat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Menu created on {self.creation_date}"
