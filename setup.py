import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read() 

setuptools.setup( 
name = "projekt", 
version = "0.0.1", 
author = "Kian Büchner", 
author_email = "kbuechner@stud.macromedia.de", 
description = "A small example package - for how to upload on Github", 
long_description = long_description, long_description_content_type = "text/markdown", 
url = "https://github.com/kianbuechner/projekt", project_urls = { "Bug Tracker": "https://github.com/kianbuechner/projekt/issues", }, license='MIT', 
packages=['projekt'], install_requires=['requests'], 
) 