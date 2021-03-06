# Generated by Django 3.1.4 on 2021-02-19 08:10

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offerride', '0004_delete_offerride'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('number', models.IntegerField()),
                ('departure', models.TimeField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
    ]
