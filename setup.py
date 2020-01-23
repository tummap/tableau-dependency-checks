import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    setup_requires=['wheel'],
     name='TabluFields',  
     version='1.0',
     scripts=['ReadTWBFiles/ReadTWBFiles.py'] ,
     author="Praveen Kumar",
     author_email="pkumar.tummala@gmail.com",
     description="Reads Tableau XML files from a specified directory for all used columns",
     long_description=long_description,
     url="https://github.com/tummap/tableau-dependency-checks/",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3"
       
     ],
 )
