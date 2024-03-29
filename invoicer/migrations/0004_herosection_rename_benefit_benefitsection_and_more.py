# Generated by Django 4.2.9 on 2024-01-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0003_benefit'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subheadline', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Benefit',
            new_name='BenefitSection',
        ),
        migrations.RenameModel(
            old_name='Feature',
            new_name='FeatureSection',
        ),
    ]
