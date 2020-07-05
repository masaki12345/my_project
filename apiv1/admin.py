from django.contrib import admin
from reversion.admin import VersionAdmin
# Register your models here.
from .models import User

admin.site.register(User, VersionAdmin)
