from django.db import models
from django.db import connection, connections

# Create your models here.
class BookInfo(models.Model) :
    bookname=models.CharField(max_length=26)
    bookauth=models.CharField(max_length=10)
    bookid=models.IntegerField(primary_key=True)
    bookstore=models.IntegerField(default=0)
    # def bookstore(self):
    #     cursor = connection.cursor()  # cursor = connections['default'].cursor()
    #     cursor.execute('select sum(buynum) from bookmanagement_bookbuyinfo where bookinfos_id=%d;'%self.bookid)
    #     ret = cursor.fetchone()[0]
    #     cursor.execute('select sum(lenum) from bookmanagement_bookleaseinfo where bookinfos_id=%d;'%self.bookid)
    #     ret2 = cursor.fetchone()[0]
    #     cursor.execute('select sum(obnum) from bookmanagement_bookobsoinfo where bookinfos_id=%d;'%self.bookid)
    #     ret3 = cursor.fetchone()[0]
    #     retnum=0
    #     if ret is not None:
    #         if ret2 is not None:
    #             if ret3 is not None:
    #                 retnum=ret-ret2-ret3
    #             return (ret-ret3,)
    #         if ret3 is None:
    #             return (ret-ret2,)
    #             #num=BookBuyInfo.objects.raw('select sum(buynum) from bookmanagement_bookbuyinfo;')
    #     return (ret-ret2-ret3,)

    def __str__(self):
        return self.bookname

class BookBuyInfo(models.Model):
    bookinfos=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    buytime=models.DateTimeField(primary_key=True)
    buynum=models.IntegerField()
    
    # def __str__(self):
    #     return self.buytime.__str__

class BookObsoInfo(models.Model):
    bookinfos=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    obtime=models.DateTimeField(primary_key=True)
    obnum=models.IntegerField()

    def __str__(self):
        return self.bookinfos.bookname

class BookLeaseInfo(models.Model):
    bookinfos=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    Letime=models.DateTimeField(primary_key=True)
    Lenum=models.IntegerField()
    Letarget=models.CharField(max_length=10)

    def __str__(self):
        return self.bookinfos.bookname

# class BookStorage(models.Model):
#     bookinfos=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
#     bookstoretotal=BookInfo.objects.raw('select sum(buynum) from bookmanagement_bookbuyinfo;')

