# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_projectimage_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='main_image',
            field=models.ImageField(default=1, upload_to=b'images/project'),
            preserve_default=False,
        ),
    ]
