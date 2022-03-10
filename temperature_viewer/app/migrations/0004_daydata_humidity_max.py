# Generated by Django 3.2.12 on 2022-03-10 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_daydata_humidity_ave_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='daydata',
            name='humidity_max',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='humidity_max', to='app.timedata'),
        ),
    ]
