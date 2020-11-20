# Generated by Django 3.1.3 on 2020-11-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='read', to='posts.Post'),
        ),
    ]
