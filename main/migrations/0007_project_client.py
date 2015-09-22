# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150922_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
