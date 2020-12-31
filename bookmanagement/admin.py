from django.contrib import admin
from bookmanagement.models import BookInfo
from bookmanagement.models import BookBuyInfo
from bookmanagement.models import BookObsoInfo
from bookmanagement.models import BookLeaseInfo
from django.db import connection, connections
from bs4 import BeautifulSoup

admin.site.site_header = '书籍管理系统'  # config header
admin.site.site_title = 'bookmanager'


class BookInfoAdmin(admin.ModelAdmin):
    list_display=['bookid','bookname','bookauth','bookstore']
    
class BookBuyInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','buytime','buynum']

class BookObInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','obtime','obnum']
    def save_model(self, request, obj, form, change):
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select sum(obnum) from bookmanagement_bookinfo where bookinfos_id=%d;'%obj)
        ret = cursor.fetchone()[0]
        soup = BeautifulSoup(form,'lxml')
        obsoletenum=int(soup.find_all('input')[2]["value"])
        if obsoletenum < ret:
            super().save_model(request, obj, form, change)


class BookLeInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','Letime','Lenum','Letarget']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookBuyInfo,BookBuyInfoAdmin)
admin.site.register(BookObsoInfo,BookObInfoAdmin)
admin.site.register(BookLeaseInfo,BookLeInfoAdmin)
