# Generated by Django 4.0.5 on 2022-08-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_fine_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]