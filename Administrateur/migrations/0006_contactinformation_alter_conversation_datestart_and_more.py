# Generated by Django 4.1.5 on 2023-06-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrateur', '0005_alter_conversation_datestart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='conversation',
            name='dateStart',
            field=models.CharField(default='2023-06-05 20:22:46', max_length=100),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='dateUpdated',
            field=models.CharField(default='2023-06-05 20:22:46', max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='dateEnvoie',
            field=models.CharField(default='2023-06-05 20:22:46', max_length=100),
        ),
    ]
