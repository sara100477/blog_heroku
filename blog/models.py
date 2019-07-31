from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    user_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title