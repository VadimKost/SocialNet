# Generated by Django 2.2 on 2020-10-27 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField(blank=True, default='', max_length=128)),
                ('AboutMe', models.TextField(blank=True, default='', max_length=256)),
                ('data', models.DateField()),
                ('gender', models.CharField(choices=[(1, 'Man'), (2, 'Woman'), (3, 'Other')], max_length=32)),
                ('photo', models.ImageField(blank=True, default='default/defaultPhoto.png', upload_to='media/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactAndLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=32)),
                ('link', models.CharField(blank=True, default='', max_length=1024)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_and_links', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
