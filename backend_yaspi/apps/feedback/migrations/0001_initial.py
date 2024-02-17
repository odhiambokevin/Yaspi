# Generated by Django 5.0.2 on 2024-02-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('posted_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
                'db_table': 'feedback',
                'ordering': ['-posted_on'],
            },
        ),
    ]