# Generated by Django 4.2.3 on 2023-07-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0006_usercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
