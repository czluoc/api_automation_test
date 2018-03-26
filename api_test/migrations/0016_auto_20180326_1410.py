# Generated by Django 2.0.2 on 2018-03-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0015_auto_20180323_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiparameter',
            name='required',
            field=models.BooleanField(default=True, verbose_name='是否必填'),
        ),
        migrations.AlterField(
            model_name='apiresponse',
            name='required',
            field=models.BooleanField(default=True, verbose_name='是否必含'),
        ),
    ]
