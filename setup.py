from distutils.core import setup

setup(
    name='django-orderedmodel',
    version='1.0',
    description='intends to help you create Django models which can be moved up\down (or left\right) with respect to each other.',
    author='Kirill Elagin',
    author_email='kirelagin@gmail.com',
    url='https://github.com/kirelagin/django-orderedmodel',
    packages = [
        'orderedmodel'
    ],
    package_data = {'orderedmodel': [
        'static/orderedmodel/arrow-down.gif',
        'static/orderedmodel/arrow-up.gif'
    ]}
)



