# Generated by Django 2.1.7 on 2020-01-18 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200118_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customuser.CustomUser'),
        ),
    ]
