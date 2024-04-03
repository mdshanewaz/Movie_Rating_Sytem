from django.db import models
from Login_App.models import CustomUesr
from Movie_App.models import MovieModel

# Create your models here.

class MovieUserRatingModel(models.Model):

    RATE_CHOICES = (
    (0.0, 0.0), (0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (1.5, 1.5), (1.6, 1.6), (1.7, 1.7), (1.8, 1.8), (1.9, 1.9), (2.0, 2.0), (2.1, 2.1), (2.2, 2.2), (2.3, 2.3), (2.4, 2.4), (2.5, 2.5), (2.6, 2.6), (2.7, 2.7), (2.8, 2.8), (2.9, 2.9), (3.0, 3.0), (3.1, 3.1), (3.2, 3.2), (3.3, 3.3), (3.4, 3.4), (3.5, 3.5), (3.6, 3.6), (3.7, 3.7), (3.8, 3.8), (3.9, 3.9), (4.0, 4.0), (4.1, 4.1), (4.2, 4.2), (4.3, 4.3), (4.4, 4.4), (4.5, 4.5), (4.6, 4.6), (4.7, 4.7), (4.8, 4.8), (4.9, 4.9), (5.0, 5.0),
)

    user = models.ForeignKey(CustomUesr, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, null=True)
    rate = models.FloatField(choices=RATE_CHOICES, null=True)
    
    def __str__(self):
        return str(self.rate)

