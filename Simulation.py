import random, sys
from Person import Person
from Virus import Virus
from FileWriter import FileWriter

class Simulation:
  
    def __init__(self, initial_vaccinated, initial_infected, initial_healthy, virus, resultsfilename):
        '''Set up the initial simulation values'''

        self.virus = virus 
        self.initial_infected = initial_infected 
        self.initial_healthy = initial_healthy
        self.initial_vaccinated = initial_vaccinated

        self.population = []

        self.population_size = initial_infected + initial_healthy + initial_vaccinated


        self.total_dead = 0
        self.total_vaccinated = initial_vaccinated

        self.file_writer = FileWriter(resultsfilename)


    def create_population(self):
        '''Creates the population (a list of Person objects) consisting of initial infected people, initial healthy non-vaccinated people, and 
        initial healthy vaccinated people. Adds them to the population list'''

        for i in range(self.initial_infected):
        	person = Person(False, virus)
        	self.population.append(person)

        for i in range(self.initial_healthy):
            person = Person(False, None)
            self.population.append(person)

        for i in range(self.initial_vaccinated):
            person = Person(True, None)
            self.population.append(person)
        	
    def print_population(self):
        for person in self.population:
            print(person.is_alive)
            print(person.is_vacinated)
            print(person.infection)
        '''Prints out every person in the population and their current attributes'''
      

    def get_infected(self):
        infected= []
        for person in self.population:
            if person.infection != None:
                infected.appened(person)
        return infected


    

        '''Gets all the infected people from the population and returns them as a xlist'''
        #TODO: finish this method

    def simulation_should_continue(self):
        vaccinated = 0 
        infected = 0

        for person in self.population: 
            if person.is_alive and person.is_vaccinated:
                vaccinated += 1 
            if person.is_alive == False:
                self.total_dead += 1 
            if person.infection is not None:
                infected += 1 
        if infected == 0 and (self.total_vaccinated or self.total_dead == self.population_size):
            return False
        elif self.total_vaccinated == self.population_size:
            return False
        elif self.total_dead == self.population_size:
            return False
        else: 
            return True 

        '''Determines whether the simulation should continue.
        If everyone in the population is dead then return False, the simulation should not continue
        If everyone in the population is vaccinated return False
        If there are no more infected people left and everyone is either vaccinated or dead return False
        In all other cases return True'''
        #TODO: finish this method
        

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        
        self.create_population()
        random.shuffle(self.population)

        self.print_population()
        
        time_step_counter = 0
        should_continue = True

        self.file_writer.init_file(self.virus, self.population_size, self.initial_vaccinated, self.initial_healthy, self.initial_infected)

        #keep looping until the simulation ends
        while self.simulation_should_continue():

            #save the current infected
            old_infected = self.get_infected()
            self.time_step(old_infected)
            #time step will create newly infected people, just determine the survivial of the previous infected people
            self.determine_survival(old_infected)

            time_step_counter += 1

        print(f'The simulation has ended after {time_step_counter} turns.')
        self.file_writer.write_results(time_step_counter, self.total_dead, self.total_vaccinated)

    def determine_survival(self, infected):
        for infected_person in infected:
            infected_person.did_survive_infection()
            if False:
                infected_person.is_alive = False
                infected_person.infection = None
                self.total_dead += 1
            else:
                infected_person.is_alive = True
                infected_person.infection = None
                infected_person.is_vaccinated = True
                self.total_vaccinated += 1
       




      


    def time_step(self, infected):
        ''' For every infected person interact with a random person from the population 10 times'''

        for infected_person in infected:
            for i in range(10):
                random_index = random.randrange(0, self.population_size)
                random_person = self.population[random_index]
                self.interaction(infected_person, random_person)



    def interaction(self, infected, random_person):
        assert infected.is_alive == True 
        assert random_person.is_alive == True

        if random_person.is_vaccinated == False:
            num = random.randint(0,1)
            if num < reproduction_num:
                random_person.infection = True
            else:
                random_person.is_vaccinated = True
                self.total_vaccinated += 1

if __name__ == "__main__":

    #Set up the initial simulations values
    virus_name = "Malaise"
    reproduction_num = 0.20
    mortality_num = .99

    initial_healthy = 10
    initial_vaccinated = 5

    initial_infected = 1

    virus = Virus(virus_name, reproduction_num, mortality_num)

    simulation = Simulation(initial_vaccinated, initial_infected, initial_healthy, virus, "results.txt")

    #run the simulation
    simulation.run()












