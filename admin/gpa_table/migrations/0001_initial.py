# Generated by Django 3.0.8 on 2020-08-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GpaTable',
            fields=[
                ('field_id', models.CharField(db_column='_id', max_length=500)),
                ('course_comb', models.CharField(db_column='Course_Comb', max_length=255, primary_key=True, serialize=False)),
                ('subject', models.CharField(db_column='Subject', max_length=300)),
                ('number', models.CharField(db_column='Number', max_length=300)),
                ('course_title', models.CharField(db_column='Course_Title', max_length=300)),
                ('a_plus', models.CharField(db_column='A_plus', max_length=50)),
                ('a_standard', models.CharField(db_column='A_standard', max_length=50)),
                ('a_minus', models.CharField(db_column='A_minus', max_length=50)),
                ('b_plus', models.CharField(db_column='B_plus', max_length=50)),
                ('b_standard', models.CharField(db_column='B_standard', max_length=50)),
                ('b_minus', models.CharField(db_column='B_minus', max_length=50)),
                ('c_plus', models.CharField(db_column='C_plus', max_length=50)),
                ('d_plus', models.CharField(db_column='D_plus', max_length=50)),
                ('c_minus', models.CharField(db_column='C_minus', max_length=50)),
                ('d_minus', models.CharField(db_column='D_minus', max_length=50)),
                ('c_standard', models.CharField(db_column='C_standard', max_length=50)),
                ('d_standard', models.CharField(db_column='D_standard', max_length=50)),
                ('f', models.CharField(db_column='F', max_length=50)),
                ('average_grade', models.CharField(db_column='Average_Grade', max_length=300)),
                ('primary_instructor', models.CharField(db_column='Primary_Instructor', max_length=300)),
            ],
            options={
                'db_table': 'GPA_TABLE',
                'managed': False,
            },
        ),
    ]
