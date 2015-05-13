__author__ = 'qiong'

# start time 9:16pm
# end time 9:34 pm
# time complexity: O(n)
# space complexity: O(n)

# input is a string with integers and operators, separated by white spaces
def expression_eval(t):
    stack = []
    idx = 0
    s = t.split()
    while idx<len(s):
        # meets a symbol, then pop the top two numbers and push the result
        if s[idx]=='+' or s[idx]=='-' or s[idx]=='*' or s[idx]=='/':
            if len(stack)>=2:
                x = stack.pop()
                y = stack.pop()
            else:
                print('not enough operands')
                raise RuntimeError
            if s[idx]=='+':
                stack.append(x+y)
            elif s[idx]=='-':
                stack.append(x-y)
            elif s[idx]=='*':
                stack.append(x*y)
            else:
                stack.append(x/y)
        else:
            # meets a number then add to the stack
            stack.append(int(s[idx]))
        idx += 1
    if len(stack)==1:
        return stack[0]
    else:
        print('not enough operators')
        raise RuntimeError

# test cases:
s = '4 5 +'
s = '4 +'
s = '4 5 * 3 +'
s = '4 5 / 2 5 * + '
s = '4 5 / 2 5 *'
print expression_eval(s)