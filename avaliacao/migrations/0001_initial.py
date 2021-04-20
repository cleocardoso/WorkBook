# Generated by Django 2.2.9 on 2021-03-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=250, verbose_name='descricao')),
                ('nota', models.IntegerField(blank=True, null=True, verbose_name='nota')),

            ],
            options={
                'db_table': 'avaliacao',
            },
        ),
    ]
