# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GpaTable(models.Model):
    field_id = models.CharField(db_column='_id', max_length=500)  # Field renamed because it started with '_'.
    course_comb = models.CharField(db_column='Course_Comb', primary_key=True, max_length=300)  # Field name made lowercase.
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


class GenEd(models.Model):
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=500)  # Field renamed because it started with '_'.
    course_comb = models.CharField(db_column='Course_Comb', max_length=500)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=50)  # Field name made lowercase.
    course_title = models.CharField(db_column='Course_title', max_length=500)  # Field name made lowercase.
    acp = models.CharField(db_column='ACP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs = models.CharField(db_column='CS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hum = models.CharField(db_column='HUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nat = models.CharField(db_column='NAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qr = models.CharField(db_column='QR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sbs = models.CharField(db_column='SBS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gen_ED'


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


class StudentMisc(models.Model):
    email = models.CharField(db_column='email_Id', primary_key=True,max_length=255)  # Field name made lowercase.
    major_taken = models.CharField(db_column='Major_Taken', max_length=50)  # Field name made lowercase.
    major_percentile = models.CharField(db_column='Major_Percentile', max_length=50)  # Field name made lowercase.
    gened_taken = models.CharField(db_column='Gened_Taken', max_length=50)  # Field name made lowercase.
    gened_percentile = models.CharField(db_column='Gened_Percentile', max_length=50)  # Field name made lowercase.
    current_gpa = models.CharField(db_column='Current_GPA', max_length=50)  # Field name made lowercase.
    hours_completed = models.CharField(db_column='Hours_Completed', max_length=50)  # Field name made lowercase.
    target_gpa = models.CharField(db_column='Target_GPA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_MISC'


class UserAccounts(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    email_id = models.CharField(db_column='email_Id', primary_key=True, max_length=120)  # Field name made lowercase.
    password = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'User_Accounts'
