# Generated by Django 3.0.8 on 2020-08-05 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMisc',
            fields=[
                ('email', models.CharField(db_column='email_Id', max_length=255, primary_key=True, serialize=False)),
                ('major_taken', models.CharField(db_column='Major_Taken', max_length=50)),
                ('major_percentile', models.CharField(db_column='Major_Percentile', max_length=50)),
                ('gened_percentile', models.CharField(db_column='Gened_Percentile', max_length=50)),
                ('current_gpa', models.CharField(db_column='Current_GPA', max_length=50)),
                ('hours_completed', models.CharField(db_column='Hours_Completed', max_length=50)),
                ('target_gpa', models.CharField(db_column='Target_GPA', max_length=50)),
            ],
            options={
                'db_table': 'Student_MISC',
                'managed': False,
            },
        ),
    ]