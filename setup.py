from setuptools import setup, find_packages

setup(
    name='basicsetuptools',
    version='0.0.1',
    author="William Luo",
    author_email="gluo7777@gmail.com",
    description="Utilities for local automation",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points='''
        [console_scripts]
        basicsetuptools=package1.script1:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.1'
)