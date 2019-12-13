import random
from Virus import Virus

class Person:
    ''' The simulation will contain people who will make up a population.'''

    def __init__(self, is_vaccinated, infection=None):
        ''' We start out with is_alive = True
        All other values will be set by the simulation through the parameters when it instantiates each Person object.
        '''
        self.is_alive = True #boolean
        self.is_vaccinated = is_vaccinated #boolean
        self.infection = infection #virus object
        

    def did_survive_infection(self):

        rand_num = random.randint(0.0, 1.0)
        
        if rand_num < virus.mortality_num:
            person.is_alive = False
            print("done")
            return False
            
        elif rand_num > virus.mortality_num:
            person.is_vaccinated = True
            person.infection = None #May need to be False?
            print("done2")
            return True

        


if __name__ == "__main__":

    virus_name = "Malaise"
    reproduction_num = 0.20
    mortality_num = .99

    virus = Virus(virus_name,reproduction_num,mortality_num)

    person = Person(False,virus)
    person.did_survive_infection()
