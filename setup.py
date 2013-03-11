from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='pjohansson',
      version=version,
      description="My program for Pythonkurs",
      long_description="""\
              See README.md.
""",
      keywords='pythonkurs scilifelab pjohansson',
      author='Petter Johansson',
      author_email='petter.johansson@scilifelab.se',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=[
          'scripts/getting_data.py',
          'scripts/check_repo.py',
          'scripts/num_factors.py'
          ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'untangle',
          'requests',
          'pandas',
          'ipython',
          'pyzmq'
      ],
      )
