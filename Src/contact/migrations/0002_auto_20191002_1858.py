# Generated by Django 2.1.5 on 2019-10-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0', unique=True),
        ),
    ]