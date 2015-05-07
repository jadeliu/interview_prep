__author__ = 'weide'


class JSONParser:


    def parse(self, s):
        if s:

            res, _ = self.parser_help(s, 0)
            return res



    # idx is the position of first parenthesis
    # return the position of the second parenthesis
    def parser_help(self, s, idx):
        key = ''
        value = None
        dict = {}
        in_value = False
        i = idx
        while i < len(s):
            i = self.skip_ws(s, i)
            if s[i] == '{':
                if in_value == True:
                    value, i = self.parser_help(s, i)
                else:
                    key, i = self.get_string(s, i + 1)
                i += 1
            elif s[i] == ',':
                dict[key] = value
                key = ''
                value = None
                i = self.skip_ws(s, i + 1)
            elif s[i] == ':':
                in_value = True
                i += 1
            elif s[i] == '"':  # value is string
                value, i = self.get_string(s, i)
                i += 1
            elif s[i] == '}':
                dict[key] = value
                i += 1

        return (dict, i)


    def skip_ws(self, s, idx):
        temp = idx
        while temp < len(s):
            if s[temp] == ' ':
                temp += 1
        return temp

    def get_string(self, s, idx):
        temp = self.skip_ws(s, idx)
        if s[temp] == '"':
            left_cit = True
            temp += 1
            while temp != '"':
                temp += 1
            if left_cit:
                key = s[idx, temp + 1]
                temp += 1
            return (s[idx, temp], temp)
        return (None, None)


s = "{"here":"one"}"

parser = JSONParser()
print parser.parse(s)
