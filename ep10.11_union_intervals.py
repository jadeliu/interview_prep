__author__ = 'qiong'

# epi question 10.11
class Endpoint:
    def __init__(self, val, isClose):
        self.val = val
        self.isClose = isClose

    def __eq__(self, other):
        return self.val==other.val and self.isClose==other.isClose

    def __lt__(self, other):
        return self.val<other.val or (self.val==other.val and self.isClose==False and other.isClose==True)

    def __gt__(self, other):
        return self.val>other.val or (self.val==other.val and self.isClose==True and other.isClose==False)

    def touches(self, other):
        return self.val==other.val and self.isClose!=other.isClose

class Interval:
    def __init__(self, val1, isClose1, val2, isClose2):
        self.e1 = Endpoint(val1, isClose1)
        self.e2 = Endpoint(val2, isClose2)

    def __eq__(self, other):
        return self.e1==other.e1 and self.e2==other.e2

# input interval list
# output union interval list
def union_intervals(intervals):
    if not intervals: return None
    res = []
    intervals = sorted(intervals, key=lambda interval: interval.e1 )

    prev = intervals[0]
    for i in xrange(1, len(intervals)):
        # if two intervals has overlap
        curr = intervals[i]
        if curr.e1<=prev.e2 or curr.e1.touches(prev.e2):
            curr.e1 = prev.e1
            if curr.e2<=prev.e2:
                curr.e2 = prev.e2

        # two interval has no overlap
        # add the last interval to result
        else:
            res.append(prev)

        prev = curr
    # add last interval to list
    res.append(prev)
    return res


inter1 = Interval(0, True, 1, False)
inter2 = Interval(1, True, 2, False)
print union_intervals([inter1, inter2])
