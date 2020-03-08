# model-project
A starter repository for research code projects.

## Steps to Get Started

1. See https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template for instructions on creating a new repository using this as a template.

2. Change the name of the `thepackage` folder to have the name of your package.

3. Fill in the missing info in `setup.py`

4. Enable the `docs` folder for github pages.

5. Update the docs in `docsource`, especially `index.rst` and rebuild the docs.  
  - run `pipenv install --dev` to install all the developer dependencies.
  - run from the `make html`
  - if it looks okay, run `make github` to copy the built docs to the right folder.
