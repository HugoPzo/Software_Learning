# Generated by Django 5.1.7 on 2025-03-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_skilltag_skill_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('myRole', models.CharField(max_length=250)),
                ('tools', models.JSONField(default=list)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='skilltag',
            name='skill_image',
            field=models.ImageField(default='images/code.png', upload_to='images/'),
        ),
    ]
