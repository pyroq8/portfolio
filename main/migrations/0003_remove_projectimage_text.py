# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_projectimage_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='text',
        ),
    ]
