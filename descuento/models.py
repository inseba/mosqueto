from django.db import models

# Create your models here.
class Codigo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    fecha = models.DateField()

    def __str__(self):
        return self.code
