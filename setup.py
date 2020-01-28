import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='TabluFields',  
     version='0.1',
     scripts=['ReadTWBFiles/ReadTWBFiles.py'] ,
     author="Praveen Kumar",
     author_email="pkumar.tummala@gmail.com",
     description="Reads Tableau XML files from a specified directory for all used columns",
     long_description=long_description,
     url="https://github.com/tummap/tableau-dependency-checks/",
     packages=setuptools.find_packages(),
     install_requires=[
          'tableaudocumentapi',
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
    ]
    ,python_requires='>=3.6',
 )
