
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название подписки')),
                ('status', models.BooleanField(db_index=True, default=False, verbose_name='Статус подписки')),
                ('start_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата оформления подписки')),
                ('ended_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата окончания подписки')),
            ],
        ),
    ]
