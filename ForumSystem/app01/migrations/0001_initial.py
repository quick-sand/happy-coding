# Generated by Django 2.1.4 on 2019-07-02 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.CharField(max_length=16, verbose_name='公告id')),
                ('a_title', models.CharField(max_length=16, verbose_name='公告标题')),
                ('a_content', models.CharField(max_length=16, null=True, verbose_name='公告内容')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_id', models.CharField(max_length=16, verbose_name='分类id')),
                ('k_name', models.CharField(max_length=16, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_tid', models.CharField(max_length=16, verbose_name='帖子id')),
                ('r_uid', models.CharField(max_length=16, verbose_name='发表者id')),
                ('r_photo', models.CharField(max_length=128, null=True, verbose_name='回复的图片')),
                ('r_time', models.DateField(auto_now_add=True, verbose_name='留言时间')),
                ('r_content', models.CharField(max_length=256, verbose_name='回复内容')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.CharField(max_length=16, verbose_name='帖子id')),
                ('t_uid', models.CharField(max_length=16, verbose_name='帖子所属用户id')),
                ('t_kind', models.CharField(max_length=32, verbose_name='类别')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('t_photo', models.CharField(max_length=128, null=True, verbose_name='帖子图片')),
                ('t_content', models.CharField(max_length=3000, verbose_name='帖子正文')),
                ('t_title', models.CharField(max_length=64, verbose_name='帖子标题')),
                ('t_introduce', models.CharField(max_length=256, verbose_name='帖子简介')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16, unique=True, verbose_name='电话/用户号')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
