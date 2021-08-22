
from django.db import models


# Create your models here.

class MyGraph(models.Model):
    function_text = models.CharField(max_length=100, help_text="Введите функцию. Например: t*t+t/2.")
    graph = models.ImageField(blank=True, upload_to='img/')
    dt = models.PositiveIntegerField()
    interval = models.PositiveIntegerField()
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.function_text

    def save(self):

        from .tasks import saved_image
        saved_image.apply_async((self.id,), countdown=3)

        super().save()
        import time
        time.sleep(5)