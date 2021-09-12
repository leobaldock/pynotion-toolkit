from setuptools import find_packages, setup

setup(
    name='notion-toolkit',
    packages=find_packages(
        include=['notion-toolkit']
    ),
    version='0.1.0',
    description='A suite of tools for interacting with Notion via Python.',
    author='Leo Baldock',
    license='MIT',
    install_requires=[
        'tqdm'
    ]
)