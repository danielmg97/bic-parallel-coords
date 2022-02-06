from setuptools import setup

setup(
   name='bic_parallel_coords',
   version='1.0',
   description='A module for biclustering visualization offering improved plots based on parallel coordinates principles.',
   author='Daniel Gonçalves',
   author_email='dmateusgoncalves@tecnico.ulisboa.pt',
   packages=['bic_parallel_coords'],
   install_requires=['pandas','plotly']
)