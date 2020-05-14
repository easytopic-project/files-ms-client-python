from setuptools import setup, find_packages

setup(
    name='files-ms-client-python',
    version='0.1.0',
    url='https://github.com/maxjf1/files-ms-client-python',
    license='MIT License',
    author='Maxwell Souza',
    author_email='maxwellsouzacarvalho@gmail.com',
    keywords='client api microservice node files',
    description='Python client for Node Files Microservice',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    # test_suite='test',  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)