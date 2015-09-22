from django.db import models
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/skill')

    def __unicode__(self):
        return self.name


class Timeline(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/timeline')
    text = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    main_image = models.ImageField(upload_to='images/main_project_Image')
    text = models.TextField(null=True)
    category = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.title


class ProjectImage(models.Model):
    name = models.CharField(max_length=50, null=True)
    project = models.ForeignKey("main.Project")
    image = models.ImageField(upload_to='images/project')

    def __unicode__(self):
        return self.name
