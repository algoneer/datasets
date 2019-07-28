from distutils.core import setup
from setuptools import find_packages

setup(
    name="algoneer_datasets",
    python_requires=">=3",
    version="0.0.1",
    author="Andreas Dewes",
    author_email="andreas.dewes@algoneer.org",
    license="Creative-Commons (license of datasets varies)",
    url="https://github.com/algoneer/datasets",
    packages=find_packages(),
    install_requires=["algoneer"],
    zip_safe=False,
    entry_points={},
    description="Example datasets for Algoneer.",
    long_description="""Example datasets for Algoneer.
""",
)
