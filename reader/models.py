from django.db.models import *

# Create your models here.
# 讀者資料
class Reader(Model):
    realname = CharField('姓名', max_length=32)
    teacher_type = CharField('身分', max_length=255)
    tel = CharField('聯絡電話', max_length=255)
    email = EmailField('電子信箱')
    titleclass = CharField('職稱/任教科目', max_length=255)
    status = CharField('狀態', max_length=255)

    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.teacher_type,
            self.tel,
            self.email, 
            self.titleclass,
            self.status
        )