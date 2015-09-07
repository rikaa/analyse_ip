# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_ip', '0002_auto_20150907_1709'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IPAdress',
            new_name='IPAddress',
        ),
    ]
