# Generated by Django 2.1.15 on 2025-02-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baladeaah', '0007_auto_20250215_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photo/%y/%m/%d'),
        ),
    ]
