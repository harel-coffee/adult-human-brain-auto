from setuptools import setup, find_packages

__version__ = "0.0.0"
exec(open('cytograph/_version.py').read())

setup(
	name="cytograph",
	version=__version__,
	packages=find_packages(),
	install_requires=[
		'loompy',
		'numpy',
		'scikit-learn',
		'scipy',
		'networkx',
		'python-louvain',
		'luigi',
		'hdbscan',
		'pyyaml',
		'polo',
		'numpy-groupies'
	],
	dependency_links=['http://github.com/linnarsson-lab/numpy-groupies/tarball/master#egg=numpy_groupies'],
	
	# metadata
	author="Linnarsson Lab",
	author_email="sten.linnarsson@ki.se",
	description="Pipeline for single-cell RNA-seq analysis",
	license="MIT",
	url="https://github.com/linnarsson-lab/cytograph",
)
