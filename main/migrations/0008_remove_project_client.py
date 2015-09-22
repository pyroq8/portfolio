# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_project_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
    ]
