# Generated by Django 4.2.1 on 2023-05-31 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrateur', '0003_alter_conversation_datestart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='dateStart',
            field=models.CharField(default='2023-05-31 18:04:38', max_length=100),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='dateUpdated',
            field=models.CharField(default='2023-05-31 18:04:38', max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='dateEnvoie',
            field=models.CharField(default='2023-05-31 18:04:38', max_length=100),
        ),
    ]