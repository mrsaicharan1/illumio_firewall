# Project Title

Illumio Firewall

## Getting Started

This project consists of a python file containing a firewall class with methods to check and validate incoming and outgoing network packets. This was implemented as a part of a coding assignment for the first interview process round of Illumio, Sunnyvale, California.

### Prerequisites

This project requires the following dependencies:
1. Python 3.6
2. virtualenv(to separate dependencies from others)

### Running the script

1. To run the it on the Python REPL, fire up the terminal and run python3 shell.
2. You'd first want to import the Firewall class using `from firewall import Firewall`
3. Then you'd want to instantiate an object using `fw = Firewall('input.csv')` [here input.csv is your input file]
4. Now you can use the firewall methods.

### Solution Testing Description
Testing for the Firewall class and its usage has been done using the best practices of unit testing. A test script file has been included namely `test_firewall.py`. There are a few tests for accept_packets but we can scale this to other methods as well. Missed out due to time constraint.

## Algorithmic Approach, Design and Significant Optimizations
1. I've developed the Firewall class and its validation methods using `Test Driven Development(TDD)`. This  helped me in asserting whether the functionalities perform the task properly.

2. I had then moved onto implementing the validation method for IP addresses(`valid_ip()`). I had been able to extract the max and min IP addresses using python's slice method. I also extracted each of the octets and compared it with the packet ip address accordingly to check if it lies in the range.

3. I had used a similar approach for checking port numbers

4. If the input didn't contain ranges, I had written code to assert them directly.

5. Initially i used a line_count parameter to omit the first row in the csv file by incrementing it each time because that would contain the column names. Then I realized that if I perform this check in a loop for around 500K inputs, it would drastically affect the performance. I was able to curb this by automatically running the loop from the second input by using the csv module's `next` method.(Took care of redundant operations)

## Further Refinements and Optimizations
Due to the time constraint, I wasn't able to implement a few more helpful scripts and also optimize the existing methods. Some of them are mentioned below.
    1. The IP address could've been declared as a separate class with methods for obtaining different octets and also checking if it lies in a given range.
    2. I had also thought of writing a script to generate 500K-1M csv values and write them to a csv file to test the firewall class.


## Prospective Teams I would want to work with

I've always been interested in data analysis and performing actions which would resonate with its security using various techniques such as visualisation. I would love to work on the data team and prove my worth if I were given an opportunity for the same.

## Authors

* **Saicharan Reddy** - *Initial work* - [mrsaicharan1](https://github.com/mrsaicharan1)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
