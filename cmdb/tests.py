# -*- coding: utf-8 -*-

from django.test import TestCase

from django.http import HttpResponse

from cmdb.models import user_info


# 数据库操作：插入
def testdbinsert(request):
    test1 = user_info(name='runoob',password='123456')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 数据库操作：查询
def testdbquery(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = user_info.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = user_info.objects.filter(id=1)

    # 获取单个对象
    response3 = user_info.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = user_info.objects.order_by('name')[0:2]

    # 数据排序
    response5 = user_info.objects.order_by("id")

    # 上面的方法可以连锁使用
    response6 = user_info.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作：更新
def testdbupdate(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = user_info.objects.get(id=1)
    test1.name = 'try'
    test1.save()

    # 另外一种方式
    # user_info.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # user_info.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")



# 数据库操作：删除
def testdbdelete(request):
    # 删除id=1的数据
    test1 = user_info.objects.get(id=2)
    test1.delete()

    # 另外一种方式
    # user_info.objects.filter(id=1).delete()

    # 删除所有数据
    # user_info.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")