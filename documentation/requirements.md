# Introduction
This documentation defines requirements for our application solving the
problem of reducing size of a textfile programmatically(compressing data).
Data Compression is an interesting topic with various algorithms. I decided
to apply two of the most famous algorithms named as Huffman and Lempel Ziv
in compressing data.

### Basic Info
* **Developer's Name:** *Hamid Aebadi*
* **Developer's Study Program:**  Bachelor's in Computer Science / TKT kandidaatti
* **Project's main language:** Python (No other languages knows to review other's code than python)
* **Language used for documentation:** English


## User Requirements
 - User use the provided **Command Line Interface** to interacting with application
 - User can tell the program the filename to being compressed as Input via specifying arguments
 - User can choose algorithm to use for compresssing the data via options
 - User can choose to produce statics after compressing the data

## Application requirements
 - Application provide users with a **Command Line Interface** for interacting with program.
 - Application accepts different kinds of textfile/textfiles as argument to being compressed.
 - Application should reduce the size ofśprovided textfils about 40%-60% of the original size.
 - Application decode compressed data to original data.


# Algorithms' time and space complexity
 **Huffman's Algorithm** 
    Time-complexity: Building Huffamn Tree costs O(nlogn), encoding and decoding would be at the best case O(1)
    Space complexity is O(k) for the tree and O(n) for the decoded text


 **Lempel Ziv Algorithm**
   Time complexity: Depends mostly on implementation, it might be O(nlogn)