from setuptools import setup, find_packages

requires = ["requests>=2.25.1","urllib3>=1.26.6","beautifulsoup4>=4.11.1"]


setup(
    name='image_searcher',
    version='1.0.2',
    description='image_searcher',
    url='https://github.com/KiharaTakahiro/image_searcher',
    author='Takahiro Kihara',
    author_email='takahirokihara123@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)