# Generated by Django 2.1.4 on 2019-08-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190826_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(default='lotus.jpeg', upload_to=''),
        ),
    ]