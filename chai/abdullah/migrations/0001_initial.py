# Generated by Django 5.1.6 on 2025-03-04 02:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chaiVartity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('imge', models.ImageField(upload_to='chai')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type_chai', models.CharField(choices=[('ML', 'Masla'), ('FL', 'Fava'), ('CL', 'Cinnamon'), ('OL', 'Olive'), ('OL', 'Other')], max_length=100)),
            ],
        ),
    ]
