#Create a class called Product with attributes for name, price, and quantity.
#Implement a method to calculate the total value of the product (price * quantity).
#Create multiple objects of the Product class and calculate their total values.
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total(self):
        return self.price * self.quantity
    
product1=Product(name = "Rice",quantity= 20,price = 200)
product1.calculate_total()
product2 = Product(name="Flour",quantity=10,price=100)
product2.calculate_total()
product3 = Product(name="Soap",quantity=5,price=200)
product3.calculate_total()


#Implement a class called Student with attributes for name, age, and grades (a
#list of integers). Include methods to calculate the average grade, display the
#student information, and determine if the student has passed (average grade >=
#60). Create objects for the Student class and demonstrate the usage of these
#methods.
class Student:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        
    def average_grade(self,grades):
        count = 0
        for grade in grades:
            count += grade
            average = count / len(grade)
        if average >= 60:
            print("You have passed")
        else:
            print("You have failed")
    
    def display_information(self):
        print("Name:",{self.name})
        print("Age:",{self.age})
        print("Grade",{self.grades})
        
student = Student("Alice",24)
student.average_grade([23,67,89,40])
student.display_information()


#Create a LibraryCatalog class that handles the cataloging and management of
#books in a library. Implement methods to add new books, search for books by
#title or author, keep track of available copies, and display book details.
class LibraryCatalog:
    def __init__(self,book,author,copies):
        self.book = book
        self.author = author
        self.copies = copies
        
        
    def add_new_book(self,newbook,author):
        return newbook and author
    
    def search_book(self):
        self.author
    
    def display_details(self):
        print("Author:",{self.author})   
        print("Book:",{self.book})   
        
    def available_copies(self):
        return self.copies
    
library = LibraryCatalog("Born a crime","Trevor Noah",45)
library.add_new_book("Coming to birth")
library.search_book()
library.available_copies() 


   
#Ancestral Stories:** In many African cultures, the art of storytelling is passed
#down from generation to generation. Imagine you're creating an application that
#records these oral stories and translates them into different languages. The
#stories vary by length, moral lessons, and the age group they are intended for.
#Think about how you would model `Story`, `StoryTeller`, and `Translator`
#objects, and how inheritance might come into play if there are different types of
#stories or storytellers.
class OralStories:
    def __init__(self,story,strory_teller,translator):
        self.story = story
        self.stor_teller = strory_teller
        self.tranalator = translator
        
    def moral_lessons(self):
        return f"The moral lesson of {self.story} is we should adhere to do the right things all the time"
    
    def age_group(self,age):
        if age>18:
            print(f"You should listen to {self.story}") 
        else:
            print(f"You are not qualified")
        
class Mariama(OralStories):
    def __init__(self, story, strory_teller, translator):
        super().__init__(story, strory_teller, translator)
        
oral = OralStories("The witch and the man","Mwambua","Migini")
oral.moral_lessons()
oral.age_group()
mariama = Mariama("The fox and the cat","Mwangila","Mtumbili")


#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods.
class Recipe:
    def __init__(self,ingridients,prep_time,method,nutritionalInfo):
        self.ingridients = ingridients
        self.time = prep_time
        self.method = method
        self.nutritionalInfo = nutritionalInfo
    
class MoroccanRecipe(Recipe):
    def __init__(self, ingridients, prep_time, method, nutritionalInfo,fat_value,eating_time):
        super().__init__(ingridients, prep_time, method, nutritionalInfo,fat_value,eating_time)
        self.fat_value = fat_value
        self.eating_time = eating_time
        
    def get_eating_time(self):
        return f"The best time to eat is {self.eating_time} "
    
class EthopianRecipe(Recipe):
    def __init__(self, ingridients, prep_time, method, nutritionalInfo,age_group,eating_method):
        super().__init__(ingridients, prep_time, method, nutritionalInfo,age_group,eating_method)
        self.eating_method = eating_method
        self.age_group = age_group
        
    def get_eating_method(self):
        return f"The best time to eat this is{self.eating_method}"   
    
class NigerianRecipe(Recipe):
    def __init__(self, ingridients, prep_time, method, nutritionalInfo,eating_place,tribe):
        super().__init__(ingridients, prep_time, method, nutritionalInfo,eating_place,tribe) 
        self.eating_place = eating_place
        self.tribe = tribe
        
    def get_tribe(self):
        return f"The recipe is prepared mostly by {self.tribe}" 

recipe = Recipe("Tomatoes",40,"Chopping","Calcium")  
recipe2 = EthopianRecipe("Flour",50,"Mixing with water",20,"With hands") 
recipe2.get_eating_method()
recipe3 = NigerianRecipe("WheatFlour","Mixing with milk","Gives vitamins","Outside","Durubo")
recipe3.get_tribe()
recipe4 = MoroccanRecipe("Mangoes",30,"Chopping","Vitamins","High-fat value","30 minutes")
recipe4.get_eating_time()


#**Wildlife Preservation:** You're a wildlife conservationist working on a
#program to track different species in a national park. Each species has its own
#characteristics and behaviors, such as its diet, typical lifespan, migration
#patterns, etc. Some species might be predators, others prey. You'll need to





#Create a FlightBooking class that represents a flight booking system. Implement
#methods to search for available flights based on destination and date, reserve
#seats for customers, manage passenger information, and generate booking
#confirmations.
class FlightBooking:
    def __init__(self):
        self.flights = []
        self.passengers = []

    def search_flights(self, destination, date):
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                yield flight

    def reserve_seats(self, flight, passengers):
        for passenger in passengers:
            if not flight.has_available_seats():
                raise ValueError("Not enough seats available on flight.")
            flight.reserve_seat()

    def manage_passenger_information(self, passenger, information):
        passenger.update_information(information)

    def generate_booking_confirmation(self, flight, passengers):
        confirmation = """
        Booking confirmation for flight {}
        Passengers: {}
        """.format(flight.id, passengers)
        return confirmation
    
booking = FlightBooking()
booking.search_flights("Morocco",30)   


       
        
            
        
             
                
          

        
        
        
            
        
            