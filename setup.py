from setuptools import setup

setup(name='ProfilR API services', 
    version='0.1',
    description='MSB & ProfilR API services', 
    url='https://profilr.forzamor.nl', 
    author='@mguikema', 
    author_email='', 
    license='MIT', 
    packages=['profilr_api_services'],
    install_requires=
    [
        'Django',
        'requests',
    ],      
    zip_safe=False)