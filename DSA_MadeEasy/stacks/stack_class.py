#  Using Lists

class stack(object):
    
    def __init__(self):
        self.content = []

    def push(self, data):
        return self.content.append(data)

    def pop(self):
        return self.content.pop()
    
    def Top(self):
        if len(self.content) > 0:
            return self.content[-1]    
        else:
            return 0
    
    def size(self):
        return len(self.content)
    
    def isEmpty(self):
        return self.size() <= 0

    def find_min(self):
        return min(self.content)
    
    def print_stack(self):
        print(self.content)


if __name__ == '__main__':
    st = stack()
    st.push(5)
    st.push(4)
    st.push(3)
    st.push(2)
    st.push(1)
    st.print_stack()
    st.pop()
    print(st.size())
    print(st.Top())
    print(st.find_min())
    st.print_stack()
    print(st.isEmpty())