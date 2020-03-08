# Prose Code

### Literate programming in Python from markdown to LaTeX

The `prosecode` library is being developed as a way to generate really neat LaTeX from markdown files.
It will support both tangling and weaving code.
That is, it can run the code from the markdown files and it can also extract the code into separate `.py` files.

## Steps to Get Started

5. Update the docs in `docsource`, especially `index.rst` and rebuild the docs.  
  - run `pipenv install --dev` to install all the developer dependencies.
  - run from the `make html`
  - if it looks okay, run `make github` to copy the built docs to the right folder.
