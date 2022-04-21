# Generated by Django 3.0 on 2022-04-21 13:17

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200501_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='media', validators=[account.models.validate_file_extension], verbose_name='Resume'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee')], max_length=10),
        ),
    ]
