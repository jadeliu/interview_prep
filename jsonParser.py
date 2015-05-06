__author__ = 'weide'


class JSONParser:
    def __init__(self):
        self.stack = []

    def parse(self, s):
        if s:
            res, _ = self.parse_help(s, 0)
            return res
    '''
    def parse_help(self, s, start):
        # return a dict and index of end pointer
        dict = {}
        idx = start
        key = ''
        value = None
        while idx<len(s):
            idx = self.skip_ws(s, idx)
            if s[idx] == '{': # when meet '{', next token should be the next string with space stripped
                self.stack.push('{')
                idx += 1
                idx = self.skip_ws(s, idx)
                temp = idx
                key, idx = self.get_string(s, idx)
                idx = self.skip_ws(s, idx)
                if s[idx]==':':
                    # meets ':', mark start of value
                    idx += 1
                    idx = self.skip_ws(s, idx)
                    if s[idx] == '{':
                        value, idx = self.parse_help(s, idx)
                    else:
                        value, idx = self.get_string(s, idx)
            elif s[idx] == ',':
                dict[key]=value
                key = ''
                value = None
            elif s[idx] == '}':
                if self.stack.pop()=='{':
                    return (dict, idx)
                else:
                    return None
        return (dict, idx)
    '''

    def parser_help(self, s, idx):
        in_paren = False
        in_

    def skip_ws(self, s, idx):
        temp = idx
        while temp<len(s):
            if s[temp]==' ':
                temp += 1
        return temp

    def get_string(self, s, idx):
        temp = idx
        if s[temp]=='"':
            self.stack.push('"')
            temp += 1
            while temp!='"':
                temp += 1
            if self.stack.pop()=='"':
                key = s[idx, temp+1]
                temp+=1
            return (s[idx, temp], temp)
        return None

s = "{\"here\":\"one\"}"

parser = JSONParser()
print parser.parse(s)
