# Generated by Django 3.1.7 on 2021-03-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_remove_college_number_of_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='how_to_get_in',
            field=models.CharField(default='You need to clear your JEE Advance Exam and get 95% above in 12th boards.', max_length=400),
            preserve_default=False,
        ),
    ]
