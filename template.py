import setuptools

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements file for dependencies
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.readlines()

__version__ = '0.1.0'

REPO_NAME = 'Chicken-Disease-Classification'
AUTHOR_USER_NAME = 'IvanSholana'
SRC_REPO = 'Chicken-Disease-Classification'
AUTHOR_EMAIL = 'ivansholana@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[req.strip() for req in requirements],  # Reading from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.9",
)
