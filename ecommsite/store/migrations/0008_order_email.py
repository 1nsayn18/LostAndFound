# Generated by Django 3.2.5 on 2021-07-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='abc@abc.com', max_length=500),
        ),
    ]