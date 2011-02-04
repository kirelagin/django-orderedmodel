OrderedModel -- orderable models models for [Django](http://www.djangoproject.com/)
========================================================

`OrderedModel` intends to help you create models which can be
moved up\\down (or left\\right) with respect to each other.

How to use it
-------------

There are a few simple steps to follow to make your models orderable:

1. `git clone git://github.com/kirelagin/django-orderedmodel.git orderedmodel`
2. Add `orderedmodel` application to your project
3. Derive your Model from `orderedmodel.models.OrderedModel`
4. Derive your ModelAdmin from `orderedmodel.admin.OrderedModelAdmin`
5. Set modelClass variable in your ModelAdmin
6. Add `reorder` field to yout ModelAdmin's `list_display`
7. Enjoy!

Now you can use `order_by('order')` in your query to get instances of your model
in desired order (actually it is not neccessary to call `order_by` explicitly
unless you have changed default ordering in your model's Meta).

Example
-------

Suppose you have a django app called _testapp_.
You need an orderable model `TestModel`.

**models.py**:

    from django.db import models
    from orderedmodel.models import OrderedModel

    class TestModel(OrderedModel):
      name = models.CharField(max_length=30)

**admin.py**:

    from django.contrib import admin
    from orderedmodel.admin import OrderedModelAdmin

    from testapp.models import TestModel


    class TestModelAdmin(OrderedModelAdmin):
      modelClass = TestModel

      list_display = ['name', 'reorder']

    admin.site.register(TestModel, TestModelAdmin)


Yep! Now if you create several instances of your model
and look into admin site you'll see something like this:

![Admin screenshot](http://kirelagin.ru/~kirrun/orderedmodel/admin.png)
