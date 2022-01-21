# Introduction
This documentation defines requirements for our application solving the
problem of reducing size of a file programmatically(compressing data). 

### Basic Info
* **Developer's Name:** *Hamid Aebadi*
* **Developer's Study Program:**  Bachelor's in Computer Science / TKT kandidaatti
* **Project's main language:** Python (No other languages knows to review other's code than python)
* **Language used for documentation:** English


# User requirements
 - User can use application without credentials (login)
 - User can select different textfile/textfiles to being compressed
 - User can deselect all selected items
 - User can compress selected items into a package
 - User can decompose all selected items into a package


# Application logic's requirements
- Application uses both Huffman coding and Lempel Ziv algorithms
- Application accepts textfiles as inputs
- Application produce a package file as output
- Application's output file's size is 40%-60% of the input's size
- Application encodes text content
- Application decodes encoded content to original content
- Application uses python language's built-in data structres

# Algorithms' time and space complexity
 **Huffman's Algorithm** 
    Time-complexity: Building Huffamn Tree costs O(nlogn), encoding and decoding would be at the best case O(1)
    Space complexity is O(k) for the tree and O(n) for the decoded text


 **Lempel Ziv Algorithm**
   Time complexity: Depends mostly on implementation, it might be O(nlogn)