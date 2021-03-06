# Generated by Django 2.1.5 on 2019-07-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('available', models.TextField(null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
