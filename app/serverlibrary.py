
def merge(array, p, q, r, byfunc):
    len_left = q - p + 1
    len_right = r - q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left_arrow = 0
    right_arrow = 0
    sort_pos = p
    while left_arrow < len_left and right_arrow < len_right:
        if byfunc(left_array[left_arrow]) <= byfunc(right_array[right_arrow]):
            array[sort_pos] = left_array[left_arrow]
            left_arrow += 1
        else:
            array[sort_pos] = right_array[right_arrow]
            right_arrow += 1
        sort_pos += 1
        
    while left_arrow < len_left:
        array[sort_pos] = left_array[left_arrow]
        left_arrow += 1
        sort_pos += 1
    while right_arrow < len_right:
        array[sort_pos] = right_array[right_arrow]
        right_arrow += 1
        sort_pos += 1

def mergesort_recursive(array, p, r, byfunc):
    if r - p > 0:
        q = (p + r) // 2
        # left array
        mergesort_recursive(array, p, q, byfunc)
        # right array
        mergesort_recursive(array, q + 1, r, byfunc)
        merge(array, p, q, r, byfunc)

def select_self(item):
    return item

def mergesort(array, byfunc=None):
    if byfunc == None:
        byfunc = select_self
    mergesort_recursive(array, 0, len(array)-1, byfunc)

# Stack class copied from mp2_exercises

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) != 0:
            return self.__items.pop()
        else:
            return None

    def peek(self):
        if len(self.__items) != 0:
            return self.__items[-1]
        else:
            return None

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.string = string

  @property
  def expression(self):
    return self.string

  @expression.setter
  def expression(self, new_expr):
    for item in new_expr:
        if item in self.valid_char:
            self.string = new_expr
        else:
            self.string = ''
            return
        
  def insert_space(self):
    new_str = ''
    for item in self.string:
        if item in '+-=*/()':
            item = ' ' + item + ' '
        new_str += item
    return new_str

  def process_operator(self, operand_stack, operator_stack):
        if operand_stack.size == 0:
            return 0
        elif operand_stack.size == 1:
            return operand_stack.pop()
        elif operand_stack.size > 1:
            right = operand_stack.pop()
            left = operand_stack.pop()
            operator = operator_stack.pop()
            if operator == '+':
                operand_stack.push(left + right)
            elif operator == '-':
                operand_stack.push(left - right)
            elif operator == '*':
                operand_stack.push(left * right)
            elif operator == '/':
                operand_stack.push(left // right)
        
        
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
#     print(expression)
    tokens = expression.split()
#     print(tokens)
    if tokens[0] == '-':
        operand_stack.push(0)
    for token in tokens:
        if token == '(':
            operator_stack.push(token)
        elif token not in '+-*/()':
            operand_stack.push(int(token))
        elif token == '+' or token == '-':
            while operator_stack.size != 0 and operator_stack.peek() != ')' and operator_stack.peek() != '(':
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(token)
        elif token == '*' or token == '/':
            while operator_stack.peek() == '*' or operator_stack.peek() == '/':
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(token)
        elif token == ')':
            while operator_stack.peek() != '(':
                self.process_operator(operand_stack, operator_stack)
            else:
                operator_stack.pop()
    while operator_stack.size != 0:
        self.process_operator(operand_stack, operator_stack)
#     print('hi', operand_stack.peek())
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





