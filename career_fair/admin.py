# Register your models here.
from django.contrib import admin

from .models import Company
from .models import Major
from .models import Location
from .models import JobType
from .models import Industry

admin.site.register(Company)
admin.site.register(Major)
admin.site.register(Location)
admin.site.register(JobType)
admin.site.register(Industry)