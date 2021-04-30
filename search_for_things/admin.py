from django.contrib import admin
from .models import Thing, StolenItem, PersonWithThing, PicturePerson, PictureStolen


admin.site.register(Thing)
admin.site.register(StolenItem)
admin.site.register(PersonWithThing)
admin.site.register(PicturePerson)
admin.site.register(PictureStolen)
