# Generated by Django 4.1.3 on 2023-01-25 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_events_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.events'),
        ),
    ]
