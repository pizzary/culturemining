# Generated by Django 3.2.19 on 2023-06-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0003_remove_patternbank_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patternbank',
            name='img',
            field=models.CharField(default='0', max_length=500),
        ),
    ]
