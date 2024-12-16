# Generated by Django 5.1.3 on 2024-12-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='message',
            name='bank_account',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=150),
        ),
    ]
