from setuptools import setup

version = {}
with open("pycoas/_version.py") as f:
    exec(f.read(), version)

setup(
    name="pycoas",
    version=version["__version__"],
    description="A simple library for dealing with complementary tasks.",
    url="https://github.com/joaopalmeiro/pycoas",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    packages=["pycoas"],
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
