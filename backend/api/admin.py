from django.contrib import admin
from .models import Apiuser
from .models import Address
from .models import Shopping
from .models import Item




admin.site.register(Apiuser)
admin.site.register(Address)
admin.site.register(Shopping)
admin.site.register(Item)

# Register your models here.
