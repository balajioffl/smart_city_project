# Generated by Django 5.2.1 on 2025-06-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0004_alter_complaintdetail_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintdetail',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
