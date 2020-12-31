from django.contrib import admin,messages
from bookmanagement.models import BookInfo
from bookmanagement.models import BookBuyInfo
from bookmanagement.models import BookObsoInfo
from bookmanagement.models import BookLeaseInfo
from django.db import connection, connections
import datetime
from bs4 import BeautifulSoup
admin.site.site_header = '书籍管理系统'  # config header
admin.site.site_title = 'bookmanager'


class BookInfoAdmin(admin.ModelAdmin):
    list_display=['bookid','bookname','bookauth','bookstore']
    search_fields = ['bookname','bookauth']
    
class BookBuyInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','buytime','buynum']
    search_fields = ['bookinfos__bookname']
    def save_model(self, request, obj, form, change):
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        curentstore = cursor.fetchone()[0]
        delta = datetime.timedelta(hours=-8)
        utctime=obj.buytime+delta
        print(utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cursor.execute('select buynum from bookmanagement_bookbuyinfo where buytime=\'%s\';'%utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cur=cursor.fetchone()
        if cur != None:
            print("not none!")
            updateOrnew = cur[0]
            updatedstore=curentstore+obj.buynum-updateOrnew
        else:
            updatedstore=curentstore+obj.buynum
        if updatedstore>=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "库存不能小于0，无法删除！")
            messages.set_level(request, messages.ERROR)
    def delete_model(self, request, obj):
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        currentstore = cursor.fetchone()[0]

        updatedstore=currentstore-obj.buynum
        if updatedstore>=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
            super().delete_model(request, obj)
        else:
            messages.error(request, "库存不能小于0，无法删除！")
            messages.set_level(request, messages.ERROR)

class BookObInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','obtime','obnum']
    search_fields = ['bookinfos__bookname']
    def save_model(self, request, obj, form, change):
        cursor = connection.cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        curentstore = cursor.fetchone()[0]
        delta = datetime.timedelta(hours=-8)
        utctime=obj.obtime+delta
        print(utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cursor.execute('select obnum from bookmanagement_bookobsoinfo where obtime=\'%s\';'%utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cur=cursor.fetchone()
        if cur != None:
            print("not none!")
            updateOrnew = cur[0]
            updatedstore=curentstore-obj.obnum+updateOrnew
        else:
            updatedstore=curentstore-obj.obnum
        if updatedstore>=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "库存不足，请重新设置，谢谢！")
            messages.set_level(request, messages.ERROR)

    def delete_model(self, request, obj):
        cursor = connection.cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        currentstore = cursor.fetchone()[0]
        updatedstore=currentstore+obj.obnum
        cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
        super().delete_model(request, obj)

class BookLeInfoAdmin(admin.ModelAdmin):
    list_display=['bookinfos','Letime','Lenum','Letarget']
    search_fields = ['bookinfos__bookname']
    def save_model(self, request, obj, form, change):
        cursor = connection.cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        curentstore = cursor.fetchone()[0]
        delta = datetime.timedelta(hours=-8)
        utctime=obj.Letime+delta
        print(utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cursor.execute('select Lenum from bookmanagement_bookleaseinfo where Letime=\'%s\';'%utctime.strftime("%Y-%m-%d %H:%M:%S"))
        cur=cursor.fetchone()
        if cur != None:
            print("not none!")
            updateOrnew = cur[0]
            updatedstore=curentstore-obj.Lenum+updateOrnew
        else:
            updatedstore=curentstore-obj.Lenum
        if updatedstore>=0:
            cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "库存不足，请重新设置，谢谢！")
            messages.set_level(request, messages.ERROR)
    def delete_model(self, request, obj):
        cursor = connection.cursor()
        cursor.execute('select bookstore from bookmanagement_bookinfo where bookname=\'%s\';'%obj.bookinfos.bookname)
        currentstore = cursor.fetchone()[0]
        updatedstore=currentstore+obj.Lenum
        cursor.execute('update bookmanagement_bookinfo set bookstore=%d where bookname =\'%s\';'%(updatedstore,obj.bookinfos.bookname))
        super().delete_model(request, obj)

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookBuyInfo,BookBuyInfoAdmin)
admin.site.register(BookObsoInfo,BookObInfoAdmin)
admin.site.register(BookLeaseInfo,BookLeInfoAdmin)
