# Generated by Django 2.1.4 on 2019-08-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190826_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='lotus.jpeg', upload_to='posts_bg'),
        ),
    ]
