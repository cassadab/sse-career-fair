# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    first_name = models.CharField(max_length=30)
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


class JobType(models.Model):
    job_type_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=255)

    def __str__(self):
        return self.job_name

    class Meta:
        db_table = "job_type"
        verbose_name_plural = 'Job Types'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    industry = models.ForeignKey('Industry', models.DO_NOTHING)
    logo_link = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website_link = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    booth_number = models.SmallIntegerField(blank=True, null=True)
    job_type = models.ManyToManyField(JobType)

    def __str__(self):
        return self.name

    def filter_job_types(self):
        return self.job_type.all()

    class Meta:
        db_table = "company"
        unique_together = (('company_id', 'name'),)
        verbose_name_plural = 'Companies'


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


class Industry(models.Model):
    industry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "industry"
        verbose_name_plural = "Industries"


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)

    def __str__(self):
        return '{}, {}'.format(self.city, self.state)

    class Meta:
        db_table = "location"


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="major")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "major"


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    major = models.ForeignKey(Major, models.DO_NOTHING, default="None")
    resume_link = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "student"
