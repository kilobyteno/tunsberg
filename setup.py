import setuptools

from tunsberg import __name__ as name
from tunsberg import __version__ as version
from tunsberg.snippane import format_version_tag

# Add README.md as long description using open() and read()
with open('README.md') as f:
    readme = f.read()

# Add requirements.txt as install_requires using open() and readlines()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name=name,
    version=version,
    description='A collection of opinionated methods, functions, classes and utils for Python, Flask and Flask-RestX.',
    long_description=readme,
    long_description_content_type='text/markdown',
    project_urls={
        'Github': 'https://github.com/kilobyteno/tunsberg',
    },
    url='https://github.com/kilobyteno/tunsberg',
    author='Kilobyte AS',
    license='MIT',
    python_requires='>=3.8',
    packages=['tunsberg'],
    include_package_data=True,
    install_requires=requirements,
    setuptools_git_versioning={
        'enabled': True,
        'dev_template': '{tag}',
        'dirty_template': '{tag}',
        'tag_formatter': format_version_tag,
    },
    setup_requires=['setuptools-git-versioning<2'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
