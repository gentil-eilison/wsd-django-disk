# Generated by Django 4.2.6 on 2023-10-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('record_label', models.CharField(max_length=100, verbose_name='Record label')),
                ('release_year', models.PositiveIntegerField(verbose_name='Release year')),
                ('country', models.CharField(max_length=150, verbose_name='Country')),
                ('genre', models.CharField(max_length=60, verbose_name='Genre')),
                ('amount_produced', models.PositiveIntegerField(verbose_name='Amount')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
    ]