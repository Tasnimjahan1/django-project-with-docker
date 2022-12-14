# Generated by Django 3.2 on 2022-10-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('age', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('cuntry', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
