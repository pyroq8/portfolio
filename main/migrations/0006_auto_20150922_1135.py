# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150922_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.ImageField(upload_to=b'images/main_project_Image'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to=b'images/project'),
        ),
    ]
