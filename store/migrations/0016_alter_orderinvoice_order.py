# Generated by Django 5.0.4 on 2024-05-20 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_transaction_options_remove_transaction_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinvoice',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.order'),
            preserve_default=False,
        ),
    ]