# Generated by Django 5.0.8 on 2024-09-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_alter_url_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='token',
            field=models.CharField(blank=True, editable=False, max_length=5, null=True, unique=True),
        ),
    ]
