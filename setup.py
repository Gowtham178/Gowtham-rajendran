import setuptools

setuptools.setup(
    include_package_data=True,
    name='math_quiz',
    version='0.0.1',
    description='Gowtham178 python module',
    url='https://github.com/Gowtham178/Gowtham-rajendran.git'
    author='Gowtham178',
    author_email='contact@Gowtham178.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='Gowtham178 python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)
