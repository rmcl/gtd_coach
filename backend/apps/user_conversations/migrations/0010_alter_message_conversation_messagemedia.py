# Generated by Django 4.2.4 on 2023-08-31 20:23

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_conversations', '0009_alter_conversation_target_alter_message_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='user_conversations.conversation'),
        ),
        migrations.CreateModel(
            name='MessageMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('file_type', models.CharField(max_length=100)),
                ('extra_details', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='user_conversations.message')),
            ],
        ),
    ]
