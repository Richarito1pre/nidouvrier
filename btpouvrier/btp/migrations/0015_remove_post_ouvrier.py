# Generated by Django 4.2.2 on 2023-07-03 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btp', '0014_rename_nombreouvrier_post_nombre_ouvrier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ouvrier',
        ),
    ]