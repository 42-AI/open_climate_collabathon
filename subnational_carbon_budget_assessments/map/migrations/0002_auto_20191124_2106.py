# Generated by Django 2.2.7 on 2019-11-24 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'ordering': ['serie', 'year']},
        ),
        migrations.RenameField(
            model_name='points',
            old_name='proj',
            new_name='serie',
        ),
    ]
