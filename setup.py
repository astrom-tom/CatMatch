from setuptools import setup
import catmatch.catmatch as cats

setup(
   name = 'catmatch',
   version = cats.__version__,
   author = cats.__credits__,
   packages = ['catmatch'],
   entry_points = {'gui_scripts': ['spartan = spartan.__main__:main',],},
   description = 'A simple catalog matching script',
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.16",
       "catscii>= 1.0",
   ],
   include_package_data=True,
)
