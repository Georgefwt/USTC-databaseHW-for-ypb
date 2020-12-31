from django.contrib import admin
from bookmanagement.models import BookInfo
from bookmanagement.models import BookBuyInfo
from bookmanagement.models import BookObsoInfo
from bookmanagement.models import BookLeaseInfo

admin.site.site_header = '书籍管理系统'  # config header
admin.site.site_title = 'bookmanager'

class BookInfoAdmin(admin.ModelAdmin):
    list_display=['bookid','bookname','bookauth','bookstore']
    
class BookBuyInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','buytime','buynum']

class BookObInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','obtime','obnum']

class BookLeInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','Letime','Lenum','Letarget']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookBuyInfo,BookBuyInfoAdmin)
admin.site.register(BookObsoInfo,BookObInfoAdmin)
admin.site.register(BookLeaseInfo,BookLeInfoAdmin)
