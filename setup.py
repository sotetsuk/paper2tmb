from setuptools import setup, find_packages

setup(
    name='paper2img',
    version="0.0.1",
    description='Convert academic papers (pdf) to nice looking images',
    author='sotetsuk',
    url='https://github.com/sotetsuk/paper2img',
    author_email='sotetsu.koyamada@gmail.com',
    license='MIT',
    install_requires=["docopt>=0.6.2"],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'paper2img = paper2img.main:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License"
    ],
    test_suite='test'
)
