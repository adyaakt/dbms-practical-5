# Generated by Django 3.0.5 on 2020-04-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_mobileno', models.IntegerField()),
                ('stu_email', models.EmailField(max_length=40)),
                ('stu_address', models.CharField(max_length=30)),
                ('stu_dept', models.CharField(max_length=30)),
                ('semister', models.IntegerField()),
            ],
        ),
    ]
