from django.db import models


# Create your models here.




class user_info(models.Model):
    '''用户表信息表'''
    def __str__(self):
        return self.username

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    username = models.CharField('用户名', max_length=20, unique=True)
    password = models.CharField('密码', max_length=128)
    sex = models.CharField('性别', max_length=8, choices=gender, default='male')
    age = models.IntegerField('年龄', null=True)
    address = models.CharField('住址', max_length=200, null=True)
    email = models.EmailField('邮箱', null=True)
    fcd = models.DateTimeField('创建时间', auto_now_add=True)
    lcd = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        db_table='user_info'     ####指定创建的表名字，否则默认是appname_tablename，例如这边是cmdb_user_info

class server_info(models.Model):
    '''主机信息表'''
    def __str__(self):
        return self.hostname
    h_status = (
        ('online','在线'),
        ('downline','下线'),
        ('unknown', '未知'),
    )

    hostname = models.CharField('主机名',max_length=16)
    ip = models.GenericIPAddressField('IP地址')
    OS = models.CharField('操作系统',max_length=12, null=True)
    admin = models.CharField('管理员账号',max_length=16, null=True)
    pwd = models.CharField('管理员密码',max_length=16, null=True)
    appname = models.CharField('应用名',max_length=16, null=True)
    status = models.CharField('主机状态',max_length=16,choices=h_status,default='unknown')
    uptime = models.DateField('上线时间',auto_now_add=True)
    downtime = models.DateField('下线时间',auto_now_add=True)
    fcd = models.DateTimeField('创建时间',auto_now_add=True)
    lcd = models.DateTimeField('最后修改时间',auto_now=True)

    class Meta:
        db_table='server_info'
