# Generated by Django 2.2.5 on 2020-03-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20200205_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]