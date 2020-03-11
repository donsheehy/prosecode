===========
The Problem
===========

Code in books is full of bugs.
This is a natural consequence of the way books and code are developed differently.
It is not common to write code in a book that can be executed in place.
The idea of having a single source document that includes both the source code and a prose description is called *Literate Programming*.

The `prosecode` library was written in response to a desire to have the following features:

- The ability to integrate executable python code into markdown files so that the output could be inserted inline.  (This is possible using the Markdown-Preview-Enhanced plugin for Atom or VS-Code).

- The ability to pull that code out into separate libraries for testing and distribution.

- The ability to provide fine-grained control over LaTeX generated from the markdown files (with executed code inline).

The main test case for the library was the generation of the book: **A First Course in Data Structures in Python**.  This open source textbook is available here <https://donsheehy.github.io/datastructures>`_
