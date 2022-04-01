from sre_compile import isstring
import stack_list as stack

class EvalExp(stack.StackList):
    """ The class CircularList based on the DoubleLinkedList allows to represent a list where
    the first and last element are connected. The list looks like a circle
    """
    
    def __init__(self):
        """ Creates an instance of class EvalExp
        input   -- self : instance of class EvalExp
        output  -- new instance of class EvalExp
        """
        # call the super class __init__ methode
        self.stack=stack.StackList()
        
    
    def evaluate(self,exp):
        operators=['+','-','*','/']
        expList=self.exp.split(" ")
        for val in expList:
            if val.isdigit():
                self.stack.push(val)
            elif val in operators:
                if not self.stack.empty_stack():
                    toPush=self.stack.mtop


                else :
                    raise Exception("Can't make calculs without numbers")
            else :
                raise Exception("Enter correct values")
