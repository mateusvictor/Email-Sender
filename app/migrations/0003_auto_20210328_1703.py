# Generated by Django 3.1.4 on 2021-03-28 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210327_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='receiver_list',
        ),
        migrations.DeleteModel(
            name='ReceiverList',
        ),
    ]
