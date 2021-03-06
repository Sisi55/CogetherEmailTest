# Generated by Django 2.2.6 on 2020-03-24 21:16

import config.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=config.utils.uuid_name_upload_to)),
                ('original_url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DevEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_identity', models.IntegerField(blank=True, default=1)),
                ('title', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField(blank=True)),
                ('external_link', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(choices=[('manual', '사이트에서 직접 입력'), ('user_request', '사용자 요청'), ('festa_crawling', 'FESTA 크롤링'), ('meetup_crawling', 'MEETUP 크롤링'), ('eventus_crawling', 'EVENTUS 크롤링'), ('facebook_crawling', 'FACEBOOK 크롤링')], default='manual', max_length=30)),
                ('status', models.CharField(choices=[('development', '개발 행사'), ('not_development', '비개발 행사'), ('unclassified_events', '미분류 행사')], default='unclassified_events', max_length=30)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Category')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Photo')),
            ],
            options={
                'ordering': ['start_at'],
            },
        ),
    ]
