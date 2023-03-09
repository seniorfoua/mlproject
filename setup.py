from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
     This function will return the list of requirements
    '''

    requirements = []

    with open(file_path, 'r') as filename:
        all_requirements = filename.readlines()
        requirements = [req.replace('\n', '') for req in all_requirements if HYPHEN_E_DOT not in req]

    return requirements



setup(
name = 'mlproject',
version = '0.0.1',
author = 'senior',
author_email =' senior@gmail.com',
packages= find_packages(),
# install_requires = ['pandas', 'numpy', 'seaborn']
install_requires = get_requirements('requirements.txt')
)



# if '__main__' == __name__:

#     print(get_requirements('requirements.txt'))