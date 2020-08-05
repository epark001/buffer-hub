from django.db import models

# Create your models here.
class StudentCourseTable(models.Model):
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=255)  # Field renamed because it started with '_'.
    email_id = models.CharField(db_column='email_Id', max_length=120)  # Field name made lowercase.
    course_comb = models.CharField(db_column='Course_Comb', max_length=300)  # Field name made lowercase.
    letter_grade = models.CharField(db_column='Letter_Grade', max_length=300)  # Field name made lowercase.
    gpa_hours = models.CharField(db_column='GPA_HOURS', max_length=300)  # Field name made lowercase.
    gpa_quality_points = models.CharField(db_column='GPA_QUALITY_POINTS', max_length=300)  # Field name made lowercase.
    primary_instructor = models.CharField(db_column='Primary_Instructor', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Course_Table'