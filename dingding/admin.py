from django.contrib import admin

admin.site.site_header='钉钉群发平台'
admin.site.site_title='钉钉'
# Register your models here.
from .models import Group
admin.site.register(Group)

from .models import Member,MemberAdmin
admin.site.register(Member,MemberAdmin)

from .models import Log,LogAdmin
admin.site.register(Log,LogAdmin)
