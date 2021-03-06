# Generated by Django 3.0 on 2022-03-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(null=True, verbose_name='出生年月'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(help_text='手机号', max_length=11, null=True, verbose_name='电话'),
        ),
    ]
