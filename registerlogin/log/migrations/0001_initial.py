# Generated by Django 3.0 on 2020-08-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMPMODEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=59)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]