# Generated by Django 2.1.7 on 2020-01-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='group.Group')),
            ],
        ),
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_comment', to='posts.Comment')),
                ('sub_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='meta_comment', to='posts.SubComment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment', to='posts.Post'),
        ),
    ]