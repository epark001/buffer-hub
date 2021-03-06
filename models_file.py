# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CourseCatalog(models.Model):
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=300)  # Field renamed because it started with '_'.
    course_comb = models.CharField(db_column='Course_Comb', max_length=300)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=300)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=300)  # Field name made lowercase.
    course_title = models.CharField(db_column='Course_Title', max_length=300)  # Field name made lowercase.
    credit_hours = models.CharField(db_column='Credit_Hours', max_length=300)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=300)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course_Catalog'


class GpaTable(models.Model):
    field_id = models.CharField(db_column='_id', max_length=300)  # Field renamed because it started with '_'.
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
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=300)  # Field renamed because it started with '_'.
    course_comb = models.CharField(db_column='Course_Comb', max_length=300)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=50)  # Field name made lowercase.
    course_title = models.CharField(db_column='Course_title', max_length=50)  # Field name made lowercase.
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
    field_id = models.CharField(db_column='_id', primary_key=True, max_length=300)  # Field renamed because it started with '_'.
    email_id = models.CharField(db_column='email_Id', max_length=120)  # Field name made lowercase.
    course_comb = models.CharField(db_column='Course_Comb', max_length=300)  # Field name made lowercase.
    letter_grade = models.CharField(db_column='Letter_Grade', max_length=300)  # Field name made lowercase.
    gpa_hours = models.CharField(db_column='GPA_HOURS', max_length=300)  # Field name made lowercase.
    gpa_quality_points = models.CharField(db_column='GPA_QUALITY_POINTS', max_length=300)  # Field name made lowercase.
    primary_instructor = models.CharField(db_column='Primary_Instructor', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_Course_Table'


class StudentMisc(models.Model):
    email_id = models.CharField(db_column='email_Id', primary_key=True, max_length=120)  # Field name made lowercase.
    major_taken = models.CharField(db_column='Major_Taken', max_length=50, blank=True, null=True)  # Field name made lowercase.
    major_percentile = models.CharField(db_column='Major_Percentile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gened_percentile = models.CharField(db_column='Gened_Percentile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    current_gpa = models.CharField(db_column='Current_GPA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hours_completed = models.CharField(db_column='Hours_Completed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    target_gpa = models.CharField(db_column='Target_GPA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_MISC'


class UserAccounts(models.Model):
    email_id = models.CharField(db_column='email_Id', primary_key=True, max_length=120)  # Field name made lowercase.
    password = models.CharField(max_length=120)
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'User_Accounts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CsvimportCsvimport(models.Model):
    model_name = models.CharField(max_length=255)
    field_list = models.TextField()
    upload_file = models.CharField(max_length=100)
    file_name = models.CharField(max_length=255)
    encoding = models.CharField(max_length=32)
    upload_method = models.CharField(max_length=50)
    error_log = models.TextField()
    import_date = models.DateField()
    import_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'csvimport_csvimport'


class CsvimportImportmodel(models.Model):
    numeric_id = models.PositiveIntegerField()
    natural_key = models.CharField(max_length=100)
    csvimport = models.ForeignKey(CsvimportCsvimport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'csvimport_importmodel'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Uiucprofs(models.Model):
    tdept = models.CharField(db_column='tDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tsid = models.CharField(db_column='tSid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    institution_name = models.CharField(max_length=50, blank=True, null=True)
    tfname = models.CharField(db_column='tFname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tmiddlename = models.CharField(db_column='tMiddlename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tlname = models.CharField(db_column='tLname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(max_length=50, blank=True, null=True)
    tnumratings = models.CharField(db_column='tNumRatings', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rating_class = models.CharField(max_length=50, blank=True, null=True)
    contenttype = models.CharField(db_column='contentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='categoryType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    overall_rating = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uiucprofs'


class UserCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    email = models.CharField(max_length=254)
    username = models.CharField(unique=True, max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_customuser'


class UserCustomuserGroups(models.Model):
    customuser = models.ForeignKey(UserCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UserCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(UserCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)
