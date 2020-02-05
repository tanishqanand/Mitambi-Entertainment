# Generated by Django 3.0.2 on 2020-02-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketing', '0002_auto_20200131_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('skills', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='influencer_detail',
            name='phone_no',
            field=models.CharField(max_length=13),
        ),
    ]
