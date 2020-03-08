# Generated by Django 2.1.7 on 2020-01-09 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
        ('posts', '0003_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='customuser.CustomUser'),
            preserve_default=False,
        ),
    ]