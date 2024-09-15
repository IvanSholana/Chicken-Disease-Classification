import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.1.0'  # Updated version

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
    long_description_content_type="text/markdown",  # Corrected the field name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[  # Add any dependencies here
        # Example: "tensorflow>=2.0.0", "numpy>=1.18.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust based on your license
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Can be updated to 'Beta', 'Stable', etc.
    ],
    python_requires=">=3.7",  # Adjust according to your Python version support
)
