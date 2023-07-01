from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    pass

projectName = 'Tribalize'
setup(
    name=projectName,
    version='0.0.0.1',
    author='Edgar Abasov',
    author_email='edgarbasov1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)