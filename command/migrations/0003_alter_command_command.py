# Generated by Django 4.1.4 on 2022-12-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
