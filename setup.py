from setuptools import setup, find_packages
import asnsreceiver

setup(
    name = 'django-asns-receiver',
    version = asnsreceiver.__version__,
    packages = find_packages(),

    author = 'Fei Tao',
    author_email = 'filia.tao@gmail.com',
    license = 'BSD',
    description = 'Reusable django app for receive Amazon SNS',
    url='https://github.com/ftao/django-asns-receiver',
    install_requires=(
        'django',
    ),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    #test_suite='tests.main',
    zip_safe = False,
)
