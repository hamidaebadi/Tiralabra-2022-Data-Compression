# Introduction
This documentation defines requirements for our application solving the
problem of reducing size of a file programmatically(compressing data). 

### Basic Infi
**Developer's Name:** *Hamid Aebadi*
**Developer's Study Program:**  Bachelor's in Computer Science / TKT kandidaatti
**Project's main language:** Python


# User requirements
 - User can use application without credentials (login)
 - User can select file/files or directory/directories to being compressed
 - User can deselect all selected items
 - User can compress selected items into a package
 - User can decompose all selected items into a package


# Application logic's requirements
- Application uses Huffman & Lempel Ziv algorithms
- Application accepts text files as inputs
- Application prouce a package file as output
- Application's output file's size is 40%-60% of the input's size
- Application encodes normal content
- Application decodes encoded content to original content
- Application uses python language's built-in data structres
