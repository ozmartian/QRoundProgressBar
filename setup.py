#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################
#
# Copyright 2017 Pete Alexandrou
#
# Ported to Python from the original works in C++ by:
#
#     Sintegrial Technologies (c) 2015
#     https://sourceforge.net/projects/qroundprogressbar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#######################################################

from setuptools import setup

setup(
    name='qroundprogressbar',
    version='1.0.0',
    packages=['.'],
    url='https://github.com/ozmartian/QRoundProgressBar',
    license='Apache License 2.0',
    author='Pete Alexandrou',
    author_email='pete@ozmartians.com',
    description='PyQt5 port of C++ circular progress bar widget library',
    keywords='qroundprogressbar PyQt PyQt5 QWidget widgets',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
