from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    label = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='movies')
    description = models.TextField()
    slug = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return(f'{self.label}')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)

        
class Ticket(models.Model):
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()


class Place(models.Model):
    ticket_id = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    number = models.IntegerField(unique=True, validators=[MaxValueValidator(20), MinValueValidator(0)])
    
