# Generated by Django 2.2.12 on 2021-08-14 22:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_auto_20210814_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='belief',
            field=otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], default=0, null=True, verbose_name='Recuerde que usted está en un grupo de 6 personas. De las otras 5 personas ¿Cuántas cree que seleccionaron el Mercado C (con contribución)?'),
        ),
    ]
