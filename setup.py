from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from the requirements.txt file."""
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
            print(f"Lines read from requirements.txt: {lines}")
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    return requirement_lst

print(get_requirements())

setup(
    name="RedWineEnd-to-End-ML",
    version="0.7",
    author="Atharva Rai",
    author_email="atharvarai07@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    license="MIT"
)
