##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os
from setuptools import setup, find_packages

setup(
    name="waitress",
    version="1.4.3",
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
