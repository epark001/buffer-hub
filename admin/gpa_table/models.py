from django.db import models

# Create your models here.
class GpaTable(models.Model):
    field_id = models.CharField(db_column='_id', max_length=500)  # Field renamed because it started with '_'.
    course_comb = models.CharField(db_column='Course_Comb', primary_key=True, max_length=255)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=300)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=300)  # Field name made lowercase.
    course_title = models.CharField(db_column='Course_Title', max_length=300)  # Field name made lowercase.
    a_plus = models.CharField(db_column='A_plus', max_length=50)  # Field name made lowercase.
    a_standard = models.CharField(db_column='A_standard', max_length=50)  # Field name made lowercase.
    a_minus = models.CharField(db_column='A_minus', max_length=50)  # Field name made lowercase.
    b_plus = models.CharField(db_column='B_plus', max_length=50)  # Field name made lowercase.
    b_standard = models.CharField(db_column='B_standard', max_length=50)  # Field name made lowercase.
    b_minus = models.CharField(db_column='B_minus', max_length=50)  # Field name made lowercase.
    c_plus = models.CharField(db_column='C_plus', max_length=50)  # Field name made lowercase.
    d_plus = models.CharField(db_column='D_plus', max_length=50)  # Field name made lowercase.
    c_minus = models.CharField(db_column='C_minus', max_length=50)  # Field name made lowercase.
    d_minus = models.CharField(db_column='D_minus', max_length=50)  # Field name made lowercase.
    c_standard = models.CharField(db_column='C_standard', max_length=50)  # Field name made lowercase.
    d_standard = models.CharField(db_column='D_standard', max_length=50)  # Field name made lowercase.
    f = models.CharField(db_column='F', max_length=50)  # Field name made lowercase.
    average_grade = models.CharField(db_column='Average_Grade', max_length=300)  # Field name made lowercase.
    primary_instructor = models.CharField(db_column='Primary_Instructor', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPA_TABLE'
        unique_together = (('course_comb', 'field_id'),)
