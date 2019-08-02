from distutils.core import setup
from setuptools import find_packages
from req import reqs

setup(
    name="algoneer_datasets",
    python_requires=">=3.5",
    version="0.0.6",
    author="Andreas Dewes",
    author_email="andreas.dewes@algoneer.org",
    license="Creative-Commons (license of datasets varies)",
    url="https://github.com/algoneer/datasets",
    packages=find_packages(),
    install_requires=[reqs],
    package_data={'algoneer_datasets': ['**/*.gz', '**/*.yml', 'py.typed']},
    zip_safe=False,
    entry_points={},
    description="Example datasets for Algoneer.",
    long_description="""Example datasets for Algoneer.
""",
)
