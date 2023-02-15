# PY4E_12.1
## Assignment
Exploring the HyperText Transport Protocol

For the purposes of this assignment we'll use this link: http://data.pr4e.org/intro-short.txt

Modify the socket1.py program to retrieve the above URL and print out the status, headers, and data with their corresponding labels.

### HINT 1: When trying to parse the header data, you can use a function like splitLines() to split the data into a list so that you can access the individual pieces of data more easily. You can also use whatever other functions make sense for parsing string data as well.

### HINT 2: The status code is the first item we get from the socket.

### HINT 3: The headers are easy to distinguish, because they are key/value pairs!

## Starting Code:
```python
import socket

def assignment_12_1():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    
    #Change this url
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

if __name__ == "__main__":    
    assignment_12_1()
```

## Expected Output:
__Note that some things will be different, like the data header!__
```
Status:
HTTP/1.1 200 OK

Headers:
Date: Wed, 15 Feb 2023 16:26:07 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

Data:
Why should you learn to write programs?

Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills.
```

## Test
When you're ready, run `pytest` to test your code!
