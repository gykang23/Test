# Generated by Django 3.2.3 on 2021-06-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_jop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rogophoto2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='회사사진')),
                ('postname2', models.CharField(max_length=50, verbose_name='제목')),
                ('author2', models.CharField(max_length=10, null=True, verbose_name='작성')),
                ('jop2', models.CharField(max_length=50, null=True, verbose_name='직업')),
                ('mainphoto2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='사진첨부')),
                ('write2', models.TextField(null=True, verbose_name='세부내용')),
                ('contents2', models.TextField(verbose_name='내용')),
                ('created_date2', models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록시')),
            ],
        ),
    ]