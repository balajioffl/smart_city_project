# Generated by Django 4.2.21 on 2025-06-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0009_faq_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_title', models.TextField(max_length=255)),
                ('new_desc', models.TextField(max_length=255)),
            ],
        ),
    ]
