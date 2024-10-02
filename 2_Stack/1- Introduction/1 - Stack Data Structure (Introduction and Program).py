class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def _push(self,item):
        self.stack.append(item)
        self.size +=1

    def _pop(self):
        self.size -= 1
        return self.stack.pop()



    def isEmpty(self):
        if len(self.stack) == 0:
            return "Stack is Empty"

        return f"Stack total element:-> {len(self.stack)}"

    def stack_top_element(self):
        if len(self.stack) > 0:
            stack_top_element = self.stack[len(self.stack)-1]
            return stack_top_element
        return "sorry stack is empty"


    def reverse_stack(self):
        return self.stack[::-1]


if __name__ == '__main__':
    s = Stack()
    s._push(10)
    s._push(20)
    s._push(30)
    s._push(40)
    s._push(50)

    # Stack all element Print
    print("Stack :->:",s.stack)

    # Stack Pop element
    print(s._pop())
    print(s._pop())
    # stack after pop element
    print("Stack :->:",s.stack)

    # call isEmpty function
    print()
    print(s.isEmpty())

    # Stack top element print
    print('\nTop Element:->', s.stack_top_element())
    print()

    # reversed Stack
    print("Stack : -->>",s.stack)
    print()
    print("Reversed Stack: ->>",s.reverse_stack())

    # Stack Size

    print("Stack size: -->>",s.size)















