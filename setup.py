from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version  = '0.0.1',
    author= "Utsav Jaiswal",
    author_email = "utsavjaiswal2004@gmail.com",
    require =  ['openai','streamlit','langchain','python-dotenv','PyPDF2'],
    packages = find_packages()
) 