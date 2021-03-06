# Generated by Django 3.2.8 on 2021-10-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='단어 내용')),
                ('type', models.CharField(blank=True, default='korean_word', max_length=10, null=True, verbose_name='언어')),
            ],
            options={
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnglishWord',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('word.word',),
        ),
        migrations.CreateModel(
            name='KoreanWord',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('word.word',),
        ),
    ]
