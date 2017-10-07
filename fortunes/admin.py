from django.contrib import admin
from .models import Fortune
from .models import User

admin.site.register(Fortune)
admin.site.register(User)
