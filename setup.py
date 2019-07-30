import re
from os import path

from setuptools import setup

github_user = 'avryhof'
github_repo_name = 'django_pyinfo'
module_path = 'django_pyinfo'
author = 'Amos Vryhof'
author_email = 'amos@vryhofresearch.com'
description = 'A phpinfo() like page for Django'


def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def find_name(*file_paths):
    name_file = read(*file_paths)
    name_match = re.search(
        r"^__name__ = ['\"]([^'\"]*)['\"]", name_file, re.M,
    )
    if name_match:
        return name_match.group(1)
    return module_path


setup(
    name=find_name(module_path, '__init__.py'),
    version=find_version(module_path, '__init__.py'),
    packages=[find_name(module_path, '__init__.py')],
    url='https://github.com/%s/%s' % (github_user, github_repo_name),
    license='MIT',
    author=author,
    author_email=author_email,
    description=description,
    long_description=read('README.md'),
    include_package_data=True,
    package_data={'': ['license.txt']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        "django",
    ],
)
