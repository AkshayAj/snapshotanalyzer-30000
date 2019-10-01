from setuptools import setup

setup(
    name='snapshotanalyzer30000',
    version='0.1',
    author='Akshay Ajgaonkar',
    author_email='ajgaonkarakshay@gmail.com',
    description="SnaphotAnalyzer30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=["shotty"],
    url="https://github.com/AkshayAj/snapshotanalyzer-30000",
    install_requires=['click', 'boto3'],
    entry_points='''
    [console_scripts]
    shotty = shotty.shotty:cli
    '''
)
