# Generated by Django 4.0.4 on 2022-08-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about_chance_coupon_fakultet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='image_url',
        ),
        migrations.AddField(
            model_name='about',
            name='telegraph',
            field=models.URLField(default=1, verbose_name='Telegraph/YouTube uchun link'),
            preserve_default=False,
        ),
    ]
