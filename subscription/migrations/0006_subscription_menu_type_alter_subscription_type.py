# Generated by Django 4.1.2 on 2022-10-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodservice', '0015_delete_subscription_delete_subscriptiontype'),
        ('subscription', '0005_alter_subscription_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='menu_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='foodservice.menutype', verbose_name='Тип меню'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='subscription.subscriptiontype', verbose_name='Тип подписки'),
        ),
    ]
