from django.contrib import admin,messages
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
    def save_model(self, request, obj, form, change):
        soup = BeautifulSoup(str(form),'lxml')
        #print(soup)
        obsoletenum=int(soup.find_all('input')[2]["value"])

        #print(type(obj))
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%str(obj))
        curentstore = cursor.fetchone()[0]
        #print(curentstore)
        updatedstore=curentstore+obsoletenum
        
        #print(updatedstore)
        cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,str(obj)))
        super().save_model(request, obj, form, change)

class BookObInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','obtime','obnum']  
    def save_model(self, request, obj, form, change):
        soup = BeautifulSoup(str(form),'lxml')
        #print(soup)
        obsoletenum=int(soup.find_all('input')[2]["value"])

        #print(type(obj))
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%str(obj))
        curentstore = cursor.fetchone()[0]
        #print(curentstore)
        updatedstore=curentstore-obsoletenum
        if updatedstore >=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,str(obj)))
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "库存不足，请重新设置，谢谢！")
            messages.set_level(request, messages.ERROR)

class BookLeInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','Letime','Lenum','Letarget']
    def save_model(self, request, obj, form, change):
        soup = BeautifulSoup(str(form),'lxml')
        #print(soup)
        obsoletenum=int(soup.find_all('input')[2]["value"])
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%str(obj))
        curentstore = cursor.fetchone()[0]
        updatedstore=curentstore-obsoletenum
        if updatedstore >=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,str(obj)))
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "库存不足，请重新设置，谢谢！")
            messages.set_level(request, messages.ERROR)

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookBuyInfo,BookBuyInfoAdmin)
admin.site.register(BookObsoInfo,BookObInfoAdmin)
admin.site.register(BookLeaseInfo,BookLeInfoAdmin)
