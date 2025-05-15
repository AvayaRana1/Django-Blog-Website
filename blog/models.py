from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return f"Message From {self.title} - {self.author}"
