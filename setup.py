from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pjohansson',
      version=version,
      description="My program for Pythonkurs",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pythonkurs scilifelab pjohansson',
      author='Petter Johansson',
      author_email='petter.johansson@scilifelab.se',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
