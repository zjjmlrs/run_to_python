#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Time    : 2017.11.25
# @Author  : zengjj
# @File    :

"""
装饰器
"""


# ====================================
# # 方法装饰方法
# def outer(some_func):
#     print "some_func", some_func.__name__
#
#     def inner(*args):          # 传入参数为装饰的方法的参数, 一般用*arge、**kwargs
#         print "before some_func"
#         ret = some_func(*args)
#         return ret + 1
#     return inner
#
#
# @outer                  # 相当于foo = outer(foo)
# def foo(x):
#    return x
#
# print foo(2)


# ===================================
# # 方法装饰class  方法一
# def outer(target):
#     print "target", target.__name__
#
#     def inner(value):
#         return target(value+1)   # 后面不能+1, 因为target(value+1)相当于初始化target类的实例，调用的是__init__,返回None
#     return inner                 # 所以只能对参数做一些额外操作
#
#
# @outer
# class TestTarget(object):
#     def __init__(self, value):  # __init__() should return None
#         print "__init__", value
#
# print TestTarget(1)


# ===================================
# # 方法装饰class 方法二: 将class保存下来 参考新框架
# # 注意并没有对该class做任何修饰，只是可以以key的形式去初始化该类的对象
# #   # 如果使用其他的方法就是导入指定文件的类，将他添加到字典中，但是可能会将其他的类错误键入
# #   # 而使用装饰器能够确定需要加载的类，确实是很方便
# target_list = dict()
#
#
# def outer(target):
#     print "target", target.__name__
#     global target_list
#     target_key = target.__name__.split("_")[1]
#     target_list[target_key] = target              # 将此类保存下来
#
#
# @outer
# class Target_1(object):
#     def __init__(self, value):
#         print "__init__", value
#
# a = target_list["1"](1)     # 取此类产生实例


# =======================================
# # 方法带参数  添加一层装饰器
# def outer_outer(string):
#     print "string", string
#
#     def outer(some_func):
#         def inter(string1):
#             return some_func(string1) + string
#         return inter
#     return outer
#
#
# @outer_outer("args1")    # 相当于add_string = outer_outer(string)(add_string)
# def add_string(string):
#     return string
# # add_string = outer_outer("test1")(add_string)
# print add_string("args2")


# =============================================
# # 类装饰器 装饰方法
# class LoginCheck(object):
#     def __init__(self, some_func):
#         print "some_func", some_func
#         self._f = some_func
#
#     # def __get__(self, instance, owner):  # 取类里面的属性时调用，对函数不起作用
#     #     print "111", instance, owner
#     #     return self._f
#
#     def __call__(self, *args):
#         if len(args) == 2:
#             return self._f(*args)
#         else:
#             return alt_function()
#
#
# def alt_function():
#     print 'Sorry - please check args'
#
#
# @LoginCheck
# def add(x, y):
#     return x + y
#
#
# # print add  # 返回LoginCheck的实例
#
# # print add(1, 3)
# # print add.__call__(1, 3)
# p = add
# print p(1, 3)   # 相当与add(1, 3)


# ===========================================
# # 类装饰器 装饰类里面的方法
# class LoginCheck(object):
#     def __init__(self, some_func):
#         print "some_func", some_func
#         self._f = some_func
#
#     def __get__(self, instance, owner):  # 取类里面的属性时调用，对函数不起作用
#         print "instance owner", instance, owner
#         self.owner = owner     # 将该类保留下来，作为参数
#         return self          # 必须返回自己，用于call
#
#     def __call__(self, *args):
#         if len(args) == 2:
#             return self._f(self.owner, *args) + 1    # 类里面的方法需要额外的self参数，所以需要__get__方法将该类保留下来
#         else:
#             return alt_function()
#
#
# def alt_function():
#     print 'Sorry - please check args'
#
#
# class Test(object):
#     @LoginCheck
#     def add(self, x, y):
#         return x + y
#
# p = Test()
# print p.add     # __get__ 返回LoginCheck的实例
# print p.add(1, 3)     # __call__
# print p.__dict__   # 为空，回去此类中找add方法，进而调用__get__方法, 猜测方法都不放进实例的__dict__中
#
# print Test.add  # get
# print Test.add(2, 5)  # __get__.__call__