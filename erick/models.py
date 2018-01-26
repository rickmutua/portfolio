from django.db import models

# Create your models here.


class Tag(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):

        return self.name


class Project(models.Model):

    tags = models.ManyToManyField(Tag)

    name = models.CharField(max_length=250)

    icon = models.ImageField(upload_to='icons')

    about = models.TextField(blank=True)

    description = models.TextField(blank=True)

    deployed_site = models.URLField(blank=True)

    github_repo = models.URLField(blank=True)

    def __str__(self):

        return self.name


class Screenshot(models.Model):

    project = models.ForeignKey('Project', blank=True, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='screenshots/', blank=True)

    def __str__(self):

        return self.name