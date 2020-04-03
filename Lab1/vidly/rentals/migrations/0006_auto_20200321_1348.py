# Generated by Django 3.0.4 on 2020-03-21 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_auto_20200321_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Genre'),
        ),
        migrations.DeleteModel(
            name='GameGenre',
        ),
    ]