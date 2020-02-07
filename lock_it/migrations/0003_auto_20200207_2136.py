# Generated by Django 3.0.2 on 2020-02-07 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lock_it', '0002_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_updated'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notes',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]