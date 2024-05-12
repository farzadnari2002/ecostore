# Generated by Django 5.0.4 on 2024-04-30 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_customer_step_customer_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'مشتریان'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'سفارشات'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('C', 'Complete'), ('F', 'Failed'), ('S', 'Sending'), ('R', 'Received')], default='P', max_length=1)),
                ('status_change', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='store.order')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=12)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='store.customer')),
            ],
            options={
                'verbose_name_plural': 'کیف پول',
            },
        ),
    ]