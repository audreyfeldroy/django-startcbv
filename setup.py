from setuptools import setup, find_packages
 
version = '0.2.3'
 
LONG_DESCRIPTION = open('README.rst').read()
 
setup(
    name='django-startcbv',
    version=version,
    description="Management command to start an app with class-based views.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django',
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='http://github.com/audreyr/django-startcbv',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
