from django.db import models

# Create your models here.
class GenEd(models.Model):
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=255)  # Field renamed because it started with '_'.
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