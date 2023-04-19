from abc import abstractclassmethod

class Musician:

    def __init__(self, name):
        self.name=name

    # Abstract class for musician
    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name) 

    # Returns a string representation of the Guitarist object
    def __str__(self):
        return f'My name is {self.name} and I play guitar'      

    # Returns a string representation of the Guitarist object
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'      

    # Returns the name of the instrument played by the Guitarist
    def get_instrument(self):
        return 'guitar'      
    
    # Returns a string of a face melting guitar solo
    def play_solo(self):
        return 'face melting guitar solo'  
       
    
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name) 

    # Returns a string representation of the Bassist object
    def __str__(self):
        return f'My name is {self.name} and I play bass'      

    # Returns a string representation of the Bassist object
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'      

    # Returns the name of the instrument played by the Bassist
    def get_instrument(self):
        return 'bass'      
    
    # Returns a string of a bass solo
    def play_solo(self):
        return "bom bom buh bom"    
    
    
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name) 

    # Returns a string representation of the Drummer object
    def __str__(self):
        return f'My name is {self.name} and I play drums'      

    # Returns a string representation of the Drummer object
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'      

    # Returns the name of the instrument played by the Drummer
    def get_instrument(self):
        return 'drums'      
    
    # Returns a string of a drum solo
    def play_solo(self):
        return "rattle boom crash"    
    
class Band:
     
     instances = []

     def __init__(self, name, members):
         """
         Initializes a Band object with a name and a list of Musician objects.
         Adds the instance to the class variable `instances`.
         """
         self.name = name
         self.members = members
         Band.instances.append(self)

     # Returns a list of solo performances by each member of the band
     def play_solos(self):
         solos = []
         for member in self.members:
             solos.append(member.play_solo())
         return solos     
         
     # Returns a string representation of the Band object
     def __str__(self):
         return f'The {self.name} is the best band ever' 
           
     # Returns a string representation of the Band object
     def __repr__(self):
         return f'{self.name}'    

     @classmethod   
     def to_list(cls):
         """
         Returns a list of all instances of Band objects.
         """
         return cls.instances 
