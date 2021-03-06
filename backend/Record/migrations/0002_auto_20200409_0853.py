# Generated by Django 3.0.5 on 2020-04-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='habit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Record.Habit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habit',
            name='current_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='habit',
            name='totall_times',
            field=models.IntegerField(default=0),
        ),
    ]
