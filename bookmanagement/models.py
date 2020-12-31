from django.db import models
from django.db import connection, connections

# Create your models here.
class BookInfo(models.Model) :
    bookname=models.CharField(max_length=26)
    bookauth=models.CharField(max_length=10)
    bookid=models.IntegerField(primary_key=True)
    def bookstore(self):
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select sum(buynum) from bookmanagement_bookbuyinfo where bookinfos_id=%d;'%self.bookid)
        ret = cursor.fetchone()
        #num=BookBuyInfo.objects.raw('select sum(buynum) from bookmanagement_bookbuyinfo;')
        return ret
    #bookstore=models.IntegerField(default=0)
    def __str__(self):
        return self.bookname

class BookBuyInfo(models.Model):
    bookinfos=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    buytime=models.DateTimeField(primary_key=True)
    buynum=models.IntegerField()

    def __str__(self):
        return self.bookinfos.bookname

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

