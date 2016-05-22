from setuptools import setup, find_packages

setup(
    name='paper2tmb',
    version="0.0.1",
    description='Convert academic papers (pdf) to nice tmb (png)',
    author='sotetsuk',
    url='https://github.com/sotetsuk/paper2tmb',
    author_email='sotetsu.koyamada@gmail.com',
    license='MIT',
    install_requires=["docopt>=0.6.2"],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'paper2tmb = paper2tmb.main:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License"
    ],
)
