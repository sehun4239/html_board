# Generated by Django 3.0.8 on 2020-08-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, verbose_name='이름')),
                ('password', models.CharField(max_length=24, verbose_name='비밀번호')),
                ('useremail', models.CharField(max_length=72, verbose_name='이메일')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
            ],
        ),
    ]
