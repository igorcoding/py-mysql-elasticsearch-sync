from setuptools import setup, find_packages

__version__ = '0.4.3'

setup(
    name='py-mysql-elasticsearch-sync',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/zhongbiaodev/py-mysql-elasticsearch-sync',
    license='MIT',
    author='Windfarer',
    author_email='windfarer@gmail.com',
    description='MySQL to Elasticsearch sync tool',
    install_requires=[
        'PyMySQL>=0.6.7',
        'mysql-replication==0.9',
        'requests==2.9.1',
        'PyYAML==3.11',
        'lxml==3.5.0',
        'future==0.15.2'
    ],
    entry_points={
        'console_scripts': [
            'es-sync=es_sync:start',
        ]
    },
    include_package_data=True
)
