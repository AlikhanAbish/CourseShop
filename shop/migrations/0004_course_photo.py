# Generated by Django 5.0.3 on 2024-05-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_uploadfiles_alter_course_students_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%y/%m/%d/', verbose_name='Photo'),
        ),
    ]