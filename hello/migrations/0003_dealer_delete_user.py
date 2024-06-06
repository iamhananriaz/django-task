# Generated by Django 5.0.6 on 2024-05-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('sale', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
