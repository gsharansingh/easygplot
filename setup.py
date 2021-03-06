import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [requirement for requirement in open('requirements.txt')]
    
setuptools.setup(
    name="easygplot",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Gursharan Singh",                     # Full name of the author
    description="`easygplot` is a python package to visualize a file's data with few commands",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",

    # packages=setuptools.find_packages(),    # List of all python modules to be installed
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],                                      # Information to filter the project on PyPi website
    # python_requires='>=3.6',                # Minimum version requirement of the package
    # py_modules=["quicksample"],             # Name of the python package
    # package_dir={'':'quicksample/src'},     # Directory of the source code of the package
    install_requires=requirements,            # Install other dependencies
    keywords="easygplot",
    name="easygplot",
    url="https://github.com/gsharansingh/easygplot",
    version='0.0.1',
)