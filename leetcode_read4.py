__author__ = 'qiong'

'''
Q:
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
Note:
The read function will only be called once for each test case.
'''

# def read4(buf)
def read(self, buf, n):
    if n == 0:
        return 0

    sofar = 0
    buf4 = ["", "", "", ""]
    nRead = read4(buf4)
    while nRead != 0 and sofar < n:
        if nRead + sofar >= n:
            for i in range(n-sofar):
                buf[sofar+i] = buf4[i]
            return n

        else:
            for i in range(nRead):
                buf[sofar+i] = buf4[i]
            sofar += nRead
            buf4 = ["", "", "", ""]
            nRead = read4(buf4)

    return sofar