# Generated by Django 3.0.2 on 2020-01-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('prod_desc', models.CharField(max_length=500)),
                ('technology', models.BooleanField(blank=True, default=False)),
                ('sports', models.BooleanField(blank=True, default=False)),
                ('gaming', models.BooleanField(blank=True, default=False)),
                ('educational', models.BooleanField(blank=True, default=False)),
                ('entertainment', models.BooleanField(blank=True, default=False)),
                ('travel', models.BooleanField(blank=True, default=False)),
                ('motivational', models.BooleanField(blank=True, default=False)),
                ('beauty', models.BooleanField(blank=True, default=False)),
                ('lifestyle', models.BooleanField(blank=True, default=False)),
                ('health', models.BooleanField(blank=True, default=False)),
                ('cooking', models.BooleanField(blank=True, default=False)),
                ('influencer_choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('queries', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='influencer_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('male', models.BooleanField(blank=True, default=False)),
                ('female', models.BooleanField(blank=True, default=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('preferred_lang', models.CharField(max_length=20)),
                ('fb_url', models.URLField(blank=True)),
                ('insta_url', models.CharField(blank=True, max_length=30)),
                ('tiktok_url', models.CharField(blank=True, max_length=30)),
                ('youtube_url', models.URLField(blank=True)),
                ('technology', models.BooleanField(blank=True, default=False)),
                ('sports', models.BooleanField(blank=True, default=False)),
                ('gaming', models.BooleanField(blank=True, default=False)),
                ('educational', models.BooleanField(blank=True, default=False)),
                ('entertainment', models.BooleanField(blank=True, default=False)),
                ('travel', models.BooleanField(blank=True, default=False)),
                ('motivational', models.BooleanField(blank=True, default=False)),
                ('beauty', models.BooleanField(blank=True, default=False)),
                ('lifestyle', models.BooleanField(blank=True, default=False)),
                ('health', models.BooleanField(blank=True, default=False)),
                ('cooking', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]