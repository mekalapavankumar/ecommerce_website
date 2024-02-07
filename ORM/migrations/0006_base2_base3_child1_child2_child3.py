# Generated by Django 4.2 on 2023-04-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0005_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base2',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Base3',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Child1',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Child2',
            fields=[
                ('base2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ORM.base2')),
                ('address', models.TextField()),
            ],
            bases=('ORM.base2',),
        ),
        migrations.CreateModel(
            name='Child3',
            fields=[
            ],
            options={
                'ordering': ['salary'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ORM.base3',),
        ),
    ]