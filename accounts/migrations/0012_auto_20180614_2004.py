# Generated by Django 2.0.1 on 2018-06-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_profilephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile_photo')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_photo',
        ),
    ]
