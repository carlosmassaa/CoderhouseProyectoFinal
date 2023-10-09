from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Avatar, Inmueble, UserProfile
from datetime import datetime

admin.site.register(Avatar)
admin.site.register(Inmueble)
admin.site.register(UserProfile)
