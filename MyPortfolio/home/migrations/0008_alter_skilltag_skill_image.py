# Generated by Django 5.1.7 on 2025-03-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_skilltag_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilltag',
            name='skill_image',
            field=models.ImageField(default='../../media/code.png', upload_to='images/'),
        ),
    ]
