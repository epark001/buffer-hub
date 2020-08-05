from django.db import models

# Create your models here.
class StudentMisc(models.Model):
    email = models.CharField(db_column='email_Id', primary_key=True,max_length=255)  # Field name made lowercase.
    major_taken = models.CharField(db_column='Major_Taken', max_length=50)  # Field name made lowercase.
    major_percentile = models.CharField(db_column='Major_Percentile', max_length=50)  # Field name made lowercase.
    gened_percentile = models.CharField(db_column='Gened_Percentile', max_length=50)  # Field name made lowercase.
    current_gpa = models.CharField(db_column='Current_GPA', max_length=50)  # Field name made lowercase.
    hours_completed = models.CharField(db_column='Hours_Completed', max_length=50)  # Field name made lowercase.
    target_gpa = models.CharField(db_column='Target_GPA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_MISC'