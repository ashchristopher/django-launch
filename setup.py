try: 
    from setuptools import setup 
except ImportError: 
  from distutils.core import setup

    
setup(
    name = 'django-launch',
    version=__import__('launch').__version__,
    description = 'Launch page for future django applications that collects users emails for future notification.',
    author = 'Ash Christopher',
    author_email = 'ash.christopher@gmail.com',
    url = 'http://github.com/ashchristopher/django-launch',
    download_url='http://github.com/ashchristopher/django-launch',
    license='MIT',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Django License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)