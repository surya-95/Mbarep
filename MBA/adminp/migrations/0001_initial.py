# Generated by Django 2.2 on 2019-04-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Add_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=30)),
                ('category', models.CharField(default='', max_length=30)),
                ('quantity', models.CharField(default='', max_length=30)),
                ('price', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Add_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('Email', models.EmailField(default='', max_length=254)),
                ('number', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
