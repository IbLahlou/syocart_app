# setup.py

from setuptools import setup, find_packages

setup(
    name='SYOCART',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "serial",
        "pandas",
        "flask"
    ],
    entry_points={
        'console_scripts': [
            'service_iot = service_iot.script:main',  #
            'service_web = service_web.app:main',  
        ],
    },
)