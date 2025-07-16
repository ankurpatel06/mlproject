from setuptools import setup, find_packages
from typing import List

hyp="-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.
    """
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyp in requirements:
            requirements.remove(hyp)
    # Remove any comments or empty lines
    return requirements
setup(
    name="mlproject",  # Your project name
    version="0.1.0",  # Initial release version
    author="Ankur",  # Your name
    author_email="ankur00ap@example.com",  # Your contact email
    description="A short description of the project",
    long_description=open("README.md").read(),  # Use README as long desc
    long_description_content_type="text/markdown",  # Markdown format
      # Project repo URL
    packages=find_packages(),  # Automatically include all packages
    include_package_data=True,  # Include files from MANIFEST.in
    install_requires=[get_requirements("requirements.txt")],  # Install dependencies
    
    classifiers=[  # Metadata for PyPI and packaging tools
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Minimum Python version required
)
