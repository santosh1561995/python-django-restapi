from django.db import models

# Create your models here.
Grade=[
    ('excellent',1),
    ('average',0),
    ('bad',-1)
]


class Post(models.Model):
    name=models.CharField(max_length=100)
    producer=models.CharField(max_length=100)
    releasedate=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=Grade,default='average',max_length=50)

    class Meta:
        ordering=['releasedate']

    def __str__(self):
        return self.name




