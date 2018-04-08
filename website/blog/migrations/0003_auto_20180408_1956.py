# Generated by Django 2.0.3 on 2018-04-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180329_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='test@test.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Hans', max_length=255),
            preserve_default=False,
        ),
    ]