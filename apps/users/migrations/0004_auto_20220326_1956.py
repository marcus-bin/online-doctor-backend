# Generated by Django 3.0 on 2022-03-26 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220326_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='users.Department', verbose_name='父类目级别'),
        ),
    ]
