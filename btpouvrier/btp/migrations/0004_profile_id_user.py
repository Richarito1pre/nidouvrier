# Generated by Django 4.2.1 on 2023-05-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btp', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
