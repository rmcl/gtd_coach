# Generated by Django 4.2.4 on 2023-08-23 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_conversations', '0002_rename_number_usernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='extra_details',
            field=models.TextField(default={}),
            preserve_default=False,
        ),
    ]
