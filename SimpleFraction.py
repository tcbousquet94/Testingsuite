
"""
Teddy Bousquet
CS5001
Keith Bagley

"""



class SimpleFraction:
    ''' class: cookie
        Attributes: Score(int), achievements(dictonary)
        Methods: Update_score, Update_file, hello3m
        Add_point and initialize_score
    '''


    def __init__(self, num, denom):
        '''
        Constructor -- creates an new instance of a fraction
        Parameters:
           self -- the current object
           num -- the numerator 
           denom -- the denominator
           returns -- num and denmon(fraction)
        '''
        if(not isinstance(num,int)):
              raise TypeError("must be a integetr")
        if(not isinstance(denom,int)):
              raise TypeError("must be a integet!")

        if(denom == 0):
            raise ZeroDivisionError ("the denominator can be zero")
        if(num == 0):
            self.num = 0
            self.denom = 1

        else:
            self.num = num
            self.denom = denom


    def validate(self):
        """
        Function: validates
        parameters: self 
        does--ensures that that num and denom are a int
        
        """
        if(not isinstance(num,int)):
              raise TypeError("must be a integer")
        if(not isinstance(denom,int)):
              raise TypeError("must be a integet!")

        if(denom == 0):
            raise ZeroDivisionError ("the denominator can be zero")
 


    def make_reciprocal(self):
        """
        Function: make_reciprocal
        parameters: self
        Does: makes current denomintor numerator and vise versa
        """
        
        new_numerator = self.denom
        new_denominator = self.num
        return SimpleFraction(new_numerator, new_denominator)
  
    def _str_(self):
        """Function-- _str_
           parameters --  self
           return: string repensation of current fraction"""
        return str(self.num)+"/"+str(self.denom)
    
    def getNum(self):
        """
        Function: getNum
        parameters: self
        return: current numerator of fraction
        """
        return int(self.num)

    def getDenom(self):
        """
        Function: getDenom
        parameters: self
        return: current denominator of fraction
        """
        return int(self.denom)
    
    def _eq_(self,other):
        """
        Function: _eq_
        parameters: self, other(fraction object)
        returns boolean seault if the are equal
        
        """
        orig = self
        
        return(orig.getNum()== other.getNum()) and (orig.getDenom() == other.getDenom())
    
    def multiply(self,other):
        """
        Function: multiply
        Parmeters: self, other(fraction object)
        does: mutiplies two fractions
        return: result as fraction
        """
        if isinstance(other,int):
            den = self.getDenom() * other
            num = self.getNum() * other
            return SimpleFraction(num,den)
        else:
            num = self.getNum() * other.getNum()
            den = self.getDenom() * other.getDenom()
            return SimpleFraction(num,den)
        

    def divide(self,other):
        """
        Function: division
        Parmeters: self, other(fraction object)
        does: divides two fractions
        return: result as fraction
        """
    
        num = self.getNum() * other.getDenom()
        den = self.getDenom() * other.getNum()
        return SimpleFraction(num,den)           





