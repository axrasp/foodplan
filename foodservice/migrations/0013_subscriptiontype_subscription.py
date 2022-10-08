# Generated by Django 4.1.2 on 2022-10-08 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodservice', '0012_auto_20221007_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('term', models.IntegerField(verbose_name='Срок подписки')),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'тип подписки',
                'verbose_name_plural': 'типы подписки',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishes', models.IntegerField(verbose_name='Количество блюд')),
                ('created_at', models.TimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('price_total', models.IntegerField()),
                ('allergens', models.ManyToManyField(blank=True, related_name='subscriptions', to='foodservice.allergen', verbose_name='Алергены')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscritions', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscritions', to='foodservice.subscriptiontype', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
    ]
