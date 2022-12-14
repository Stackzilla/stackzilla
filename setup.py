"""Setuptools configuration file."""
import os

from setuptools import setup

# Meta information
dirname = os.path.dirname(os.path.realpath(__file__))
version = open(os.path.join(dirname, 'VERSION'), encoding='utf-8').read().strip()

# Save version and author to __meta__.py
path = os.path.join(dirname, 'stackzilla', '__meta__.py')
data = (
    f'"""Package versioning info."""'
    f"# Automatically created. Please do not edit.\n"
    f"# noqa\n"
    f"__version__ = '{version}'\n"
    f"__author__ = 'Zimventures, LLC'\n"
)

with open(path, 'wb') as F:
    F.write(data.encode())

# Read in all of the requirements to install/run Stackzilla
install_requirements = []
with open('requirements.txt', encoding='utf-8') as requirements:
    for package in requirements.readlines():
        install_requirements.append(package)

# Read in all of the requirements to run the tests on the Stackzilla codebase
testing_requirements = []
with open('requirements-testing.txt', encoding='utf-8') as testing_req_fh:
    for package in testing_req_fh.readlines():
        testing_requirements.append(package)

dev_requirements = []
with open('requirements-dev.txt', encoding='utf-8') as dev_req_fh:
    for package in dev_req_fh.readlines():
        dev_requirements.append(package)

setup(
    # Basic info
    name='stackzilla',
    version=version,
    author='Zimventures, LLC',
    author_email='rob@stackzilla.dev',
    url='https://github.com/Stackzilla/stackzilla',
    description='An ORM for your application stack.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='GNU Affero General Public License v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and depencies
    package_dir={'stackzilla': 'stackzilla'},
    packages=['stackzilla.attribute',
              'stackzilla.blueprint',
              'stackzilla.cli',
              'stackzilla.database',
              'stackzilla.diff',
              'stackzilla.events',
              'stackzilla.host_services',
              'stackzilla.graph',
              'stackzilla.importer',
              'stackzilla.logger',
              'stackzilla.provider.null',
              'stackzilla.resource',
              'stackzilla.resource.compute',
              'stackzilla.utils'],
    python_requires='>3.6',
    include_package_data=True,
    install_requires=install_requirements,
    extras_require={
        'test': testing_requirements,
        'dev': dev_requirements,
    },

    # Data files
    package_data={},

    # Scripts
    entry_points={
        'console_scripts': [
            'stackzilla=stackzilla.cli.main:cli'],
    },

    # Other configurationss
    zip_safe=False,
    platforms='any',
)
