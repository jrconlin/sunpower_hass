import io
import os

from setuptools import setup, find_packages


__version__ = "0.3.0"

here = os.path.abspath(os.path.dirname(__file__))


def read_from(file):
    with io.open(os.path.join(here, file), encoding='utf8') as f:
        return f.read()


extra_options = {
    "packages": find_packages(),
}

setup(name="sunpower_hass",
      version=__version__,
      description='WIP Sunpower Solar Panel reader module.',
      long_description=read_from("README.md"),
      classifiers=["Topic :: Internet :: WWW/HTTP",
                   'Programming Language :: Python',
                   "Programming Language :: Python :: 3",
                   ],
      keywords='sunpower',
      author="jr conlin",
      author_email="src+sph@jrconlin.com",
      url='https://github.com/jrconlin/sunpower_hass',
      license="MPL2",
      test_suite="nose.collector",
      include_package_data=True,
      install_requires=read_from("requirements.txt"),
      zip_safe=False,
      tests_require=['nose', 'coverage', 'mock>=1.0.1'],
      entry_points="""
      [console_scripts]
      reading = sunpower.sunpower:main
      """,
      **extra_options
      )
