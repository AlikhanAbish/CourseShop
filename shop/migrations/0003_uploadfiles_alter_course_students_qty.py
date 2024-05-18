# Generated by Django 5.0.3 on 2024-05-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_titile_course_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='students_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
