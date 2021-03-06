# Generated by Django 3.1.7 on 2021-03-12 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('discription', models.TextField()),
                ('rank', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('website', models.URLField()),
                ('address', models.CharField(max_length=400)),
                ('is_in_wishlist', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('related_college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
            ],
        ),
    ]
