# Generated by Django 4.2.2 on 2023-07-03 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btp', '0013_rename_manoeuvre_post_nombreouvrier_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nombreOuvrier',
            new_name='nombre_ouvrier',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='typeOuvrier',
            new_name='type_ouvrier',
        ),
    ]
