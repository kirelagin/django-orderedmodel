`django-orderedmodel` -- orderable models for [Django](http://www.djangoproject.com/)
========================================================

`django-orderedmodel` intends to help you create Django models which can be
moved up/down (or left/right) with respect to each other.

How to use
-------------

There are a few simple steps to follow to make your models orderable:

1. `git clone git://github.com/kirelagin/django-orderedmodel.git`.
2. Copy (or, even better, symlink) `orderedmodel` directory to your
   Django project.
3. Add `'orderedmodel'` to `INSTALLED_APPS` in your `settings.py`.
8. Ensure that your project is [using `django.contrib.staticfiles`](https://docs.djangoproject.com/en/dev/howto/static-files/)
   to serve static content (this is now required for compatibility with Django 1.4+).
4. Derive your Model from `orderedmodel.OrderedModel`.
5. Derive your ModelAdmin from `orderedmodel.OrderedModelAdmin`.
6. Add `reorder` field to yout ModelAdmin's `list_display`.
7. Enjoy!

Now you can use `order_by('order')` in your query to get instances of your model
in desired order (actually it is not neccessary to call `order_by` explicitly
unless you have changed default ordering in your model's Meta).

Example
-------

Suppose you have a django app called _testapp_.
You need an orderable model `TestModel`.

**models.py**:

```python
from django.db import models
from orderedmodel import OrderedModel

class TestModel(OrderedModel):
  name = models.CharField(max_length=30)
```

**admin.py**:

```python
from django.contrib import admin
from orderedmodel import OrderedModelAdmin

from testapp.models import TestModel


class TestModelAdmin(OrderedModelAdmin):
  list_display = ['name', 'reorder']

admin.site.register(TestModel, TestModelAdmin)
```


Yep! Now if you create several instances of your model
and look into admin site you'll see something like this:

![Admin screenshot](http://kirelagin.ru/~kirrun/orderedmodel/admin.png)

Django versions
---------------

Current version of `django-orderedmodel` requires *Django-1.4+*.

See [branch `django-1.3`](https://github.com/kirelagin/django-orderedmodel/tree/django-1.3)
for version compatible with *Django-1.3*.
