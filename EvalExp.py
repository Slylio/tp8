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
        expList=exp.split(" ")
        for val in expList:
            if val=="+":
                res=int(self.stack.top_value())
                self.stack.pop()
                res+=int(self.stack.top_value())
                self.stack.pop()

                self.stack.push(res)
            elif val=="-":
                res=int(self.stack.top_value())
                self.stack.pop()
                res-=int(self.stack.top_value())
                self.stack.pop()

                self.stack.push(res)
            elif val=="*":
                res=int(self.stack.top_value())
                self.stack.pop()
                res*=int(self.stack.top_value())
                self.stack.pop()

                self.stack.push(res)
            elif val=="/":
                res=int(self.stack.top_value())
                self.stack.pop()
                res/=int(self.stack.top_value())
                self.stack.pop()

                self.stack.push(res)
            else :
                self.stack.push(val)
        return self.stack