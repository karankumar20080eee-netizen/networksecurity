from setuptools import find_packages,setup
from typing import List

def get_requirements()-> list[str]:
    "this function will return list of requirements"
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r")as file:
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                # ignore the empty line and -e.
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst  

  
print(get_requirements()) 

setup(
    name="networkSecurity",
    version="0.0.1",
    author="karan kumar",
    packages=find_packages(),
    install_requires=get_requirements()
    
)                       