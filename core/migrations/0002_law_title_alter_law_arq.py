# Generated by Django 5.0.6 on 2024-05-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='title',
            field=models.TextField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='law',
            name='arq',
            field=models.FileField(upload_to=''),
        ),
    ]
