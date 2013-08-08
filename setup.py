
from distutils.core import setup

setup(
    name             = 'QPygletWidget',
    version          = '0.0.1',
    author           = 'Lionel Barret',
    author_email     = 'lionel.barret@gmail.com',
    py_modules       =['qpygletwidget'],
    scripts          = [],
    url              = 'http://pypi.python.org/pypi/QPygletWidget/',
    license          = 'LICENSE.txt',
    description      = 'pyglet in pyqt',
    long_description = open('README.md').read(),
    install_requires = ['pyglet'],
    )
