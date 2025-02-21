# Generated by Django 5.0.6 on 2024-06-04 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fakult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universitet.fakultet')),
            ],
        ),
        migrations.AddField(
            model_name='fakultet',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universitet.university'),
        ),
    ]
