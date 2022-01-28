from distutils.core import setup

setup(
    name='faam_data',
    version='0.1',
    description='FAAM data standard information',
    author='Dave Sproson',
    author_email='dave.sproson@faam.ac.uk',
    url='https://github.com/FAAM-146/faam-data',
    packages=['faam_data'],
    install_requires=[
        'pydantic'
    ]
)
