# Generated by Django 2.0.1 on 2019-10-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='password',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
    ]