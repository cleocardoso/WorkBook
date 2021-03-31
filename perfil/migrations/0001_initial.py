# Generated by Django 2.2.9 on 2021-03-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='nome')),
                ('decricao', models.CharField(max_length=2000, verbose_name='descricao')),
                ('slogan', models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/')),
                ('categorias', models.ManyToManyField(to='categoria.Categoria')),
            ],
            options={
                'db_table': 'perfil',
            },
        ),
    ]
