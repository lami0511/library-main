from django.db.models import *

# Create your models here.
# 讀者資料
class Reader(Model):
    realname = CharField('姓名', max_length=32)
    teacher_type = CharField('單位處室', max_length=255)
    tel = CharField('聯絡電話', max_length=255)
    email = EmailField('電子信箱')
    titleclass = CharField('職稱/任教科目', max_length=255)
    status = CharField('教室借用(請手動填寫早上/下午/晚上，第幾節課~第幾節課使用)', max_length=255)

    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.teacher_type,
            self.tel,
            self.email, 
            self.titleclass,
            self.status
        )