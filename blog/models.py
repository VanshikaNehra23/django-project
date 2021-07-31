from django.db import models

class Blogs(models.Model):
    heading = models.CharField(max_length = 200)
    date = models.DateField()
    descr = models.TextField()

    def __str__(self):
        return self.heading