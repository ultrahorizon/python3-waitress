import os
from setuptools import setup, find_packages

setup(
    name="waitress",
    version="1.4.4",
    author="Zope Foundation and Contributors",
    author_email="zope-dev@zope.org",
    maintainer="Pylons Project",
    maintainer_email="pylons-discuss@googlegroups.com",
    description="Waitress WSGI server",
    license="ZPL 2.1",
    url="https://github.com/Pylons/waitress",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [paste.server_runner]
    main = waitress:serve_paste
    [console_scripts]
    waitress-serve = waitress.runner:run
    """,
)
