# Generated by Django 4.1.3 on 2023-01-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_rename_username_register_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoint',
            fields=[
                ('regid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('specialization', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('role', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=50)),
            ],
        ),
    ]
