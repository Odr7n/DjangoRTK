# Generated by Django 4.2.9 on 2024-01-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmdash', '0002_dashboard_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dashboard',
            options={'ordering': ['title', 'date'], 'verbose_name': 'Дашборд', 'verbose_name_plural': 'Дашборды'},
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='category',
            field=models.CharField(choices=[('Tr', 'Trigonometric'), ('Ln', 'Linear'), ('Log', 'Logarithmic')], max_length=20, verbose_name='Категории'),
        ),
    ]
