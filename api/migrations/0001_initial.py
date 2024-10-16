# Generated by Django 5.1.2 on 2024-10-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('WEB_DEV', 'Web Development'), ('ANDROID_DEV', 'Android Development'), ('DATA_SCIENCE', 'Data Science')], default='WEB_DEV')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
