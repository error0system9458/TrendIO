# Generated by Django 2.0.1 on 2018-06-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20180621_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, default='TrendIO/media/profile_phot/venice.jpg', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='profile_photo'),
        ),
    ]
