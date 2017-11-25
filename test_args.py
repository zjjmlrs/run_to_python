#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Time    :
# @Author  : zengjj
# @File    :


def fun_var_args(farg, *args):  # *args 没有key值
    print "arg:", farg
    print type(args), args   # <type 'tuple'>
    for value in args:
        print "another arg:", value

# fun_var_args(1, "two", 3)


def fun_var_kwargs(farg, **kwargs):  # **kwargs有key值
    print "arg:", farg
    print type(kwargs), kwargs   #<type 'dict'>
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

fun_var_kwargs(farg=1, myarg2="two", myarg3=3)