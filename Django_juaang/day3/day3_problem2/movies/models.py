from django.db import models

# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)

    def __str__(Model):
        return f'{Model.id}번째 영화 - {Model.title}({Model.genre})'
