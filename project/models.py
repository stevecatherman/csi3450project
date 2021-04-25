# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import ModelForm

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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


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


class Employee(models.Model):
    employeeid = models.AutoField(primary_key=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    fname = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    jobid = models.ForeignKey('Jobtype', models.DO_NOTHING, db_column='jobid', related_name='jobcode4')

    class Meta:
        managed = False
        db_table = 'employee'
        unique_together = (('employeeid', 'jobid'),)


class Jobtype(models.Model):
    jobtypeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    pay = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobtype'


class Paycheck(models.Model):
    paycheckid = models.AutoField(primary_key=True)
    gross = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    net = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    timeid = models.ForeignKey('Timecard', models.DO_NOTHING, db_column='timeid')
    empid = models.ForeignKey('Timecard', models.DO_NOTHING, db_column='empid', related_name='empcode3')
    jobid = models.ForeignKey('Timecard', models.DO_NOTHING, db_column='jobid', related_name='jobcode3')
    payid = models.ForeignKey('Timecard', models.DO_NOTHING, db_column='payid', related_name='paycode3')

    class Meta:
        managed = False
        db_table = 'paycheck'
        unique_together = (('paycheckid', 'timeid', 'empid', 'jobid', 'payid'),)


class Payperiod(models.Model):
    payperiodid = models.AutoField(primary_key=True)
    weekend = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payperiod'


class Timecard(models.Model):
    timecardid = models.AutoField(primary_key=True)
    hours = models.FloatField(blank=True, null=True)
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='empid', related_name='empcode')
    jobid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='jobid', related_name='jobcode')
    payid = models.ForeignKey(Payperiod, models.DO_NOTHING, db_column='payid', related_name='paycode')

    class Meta:
        managed = False
        db_table = 'timecard'
        unique_together = (('timecardid', 'empid', 'jobid', 'payid'),)


class Vacation(models.Model):
    vacationid = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    days = models.FloatField(blank=True, null=True)
    approver = models.CharField(max_length=45, blank=True, null=True)
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='empid', related_name='empcode2')
    jobid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='jobid', related_name='jobcode2')

    class Meta:
        managed = False
        db_table = 'vacation'
        unique_together = (('vacationid', 'empid', 'jobid'),)