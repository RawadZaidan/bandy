# Generated by Django 4.2.7 on 2024-07-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeed', '0004_company_customer_gender_freelancer_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(choices=[('BE', 'Beirut'), ('SL', 'South Lebanon'), ('ML', 'Mount Lebanon'), ('NL', 'North Lebanon'), ('AK', 'Akkar'), ('BK', 'Bekaa'), ('BH', 'Baalbak-Hermel'), ('JN', 'Jounieh')], max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='region',
            field=models.CharField(choices=[('BE', 'Beirut'), ('SL', 'South Lebanon'), ('ML', 'Mount Lebanon'), ('NL', 'North Lebanon'), ('AK', 'Akkar'), ('BK', 'Bekaa'), ('BH', 'Baalbak-Hermel'), ('JN', 'Jounieh')], max_length=2),
        ),
    ]
