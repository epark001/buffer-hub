from django.db import models
from admin.gpa_table.models import GpaTable

# Create your models here.
class StudentCourseTable(models.Model):
    email = models.CharField(db_column='email_Id', max_length=255)  # Field name made lowercase.
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=120)  # Field renamed because it started with '_'.
    course_comb = models.ForeignKey(GpaTable, models.DO_NOTHING, db_column='Course_Comb')  # Field name made lowercase.
    letter_grade = models.CharField(db_column='Letter_Grade', max_length=300)  # Field name made lowercase.
    gpa_hours = models.CharField(db_column='GPA_HOURS', max_length=300)  # Field name made lowercase.
    gpa_quality_points = models.CharField(db_column='GPA_QUALITY_POINTS', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Course_Table'