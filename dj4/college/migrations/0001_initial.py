# Generated by Django 3.1 on 2020-11-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('mag', models.TextField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
