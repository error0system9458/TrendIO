# Generated by Django 2.0.1 on 2018-06-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20180620_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='profile_photo'),
        ),
    ]
