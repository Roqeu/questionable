# Generated by Django 2.1.5 on 2020-03-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200312_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
