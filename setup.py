from setuptools import setup

setup(
    # Whatever arguments you need/want
    # Needed to silence warnings (and to be a worthwhile package)
    name='micro_tools',
    author='Anatolii Yakushko',
    author_email='shaddyx@gmail.com',
    # Needed to actually package something
    packages=['micro_tools'],
    package_dir={'micro_tools':'src/micro_tools'},
    # Needed for dependencies
    install_requires=[
                      'pytest',
                      ],
    package_data={"": ["*.json"]},
    # *strongly* suggested for sharing
    version='0.02',
    # The license can be anything you like
    license='MIT',
    description='A bunch of tools to help developing scripts',
    include_package_data=True
)
