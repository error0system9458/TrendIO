# Generated by Django 2.0.1 on 2018-05-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180531_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='social_score',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
        ),
    ]
