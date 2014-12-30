#!/usr/bin/env python

from distutils.core import setup


setup(name='django-orderedmodel',
      version='2014.12.001',

      description='Orderable models for Django',
      long_description='''
          This Django_ app helps you create Django models that can be
          moved up/down with respect to each other.

          See README_ for more details.

          .. _Django: https://www.djangoproject.com/
          .. _README: https://github.com/kirelagin/django-orderedmodel/blob/master/README.md
      ''',


      author='Kirill Elagin',
      author_email='kirelagin@gmail.com',

      url='https://github.com/kirelagin/django-orderedmodel',

      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 3',
                     'Topic :: Software Development :: Libraries',
                    ],
      keywords = ['Django', 'order', 'ordering', 'models'],

      packages = ['orderedmodel'],
      package_data = {
        'orderedmodel': [
            'static/orderedmodel/arrow-down.gif',
            'static/orderedmodel/arrow-up.gif',
        ],
      },
     )
