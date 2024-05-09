from setuptools import find_packages,setup
from typing import List

Hyp="-e ."

def get_requirement(file_path:str)->List[str]:
    
    '''
    This function will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if Hyp in requirements:
            requirements.remove(Hyp)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Suhas',
author_email='suhaspawar23@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirements.txt')





)