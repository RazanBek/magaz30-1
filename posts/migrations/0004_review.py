# Generated by Django 4.2.3 on 2023-07-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=80)),
            ],
        ),
    ]
