import os
import re
import arrow
from geopy.geocoders import Nominatim



def time_now(): # Time by chosen time zone
    time = arrow.now("Europe/Helsinki")
    return time.format("HH:mm:ss") 


def delivery_time(): # Modified time by end user
    time_now = arrow.now("Europe/Helsinki")
    time_then = time_now.replace(hour=int(delivery_time_input[0:2]), minute=int(delivery_time_input[2:4])).format("HH:mm:ss")
    return time_then


def make_dir(): # Function to make directory for the log file
    try:
        os.mkdir("Location_log")
    except FileExistsError:
        pass


def location_logfile(): # Function to write a log file
    log_file =  open("Location_log/location_log.txt", "a")
    log_file.write(location())
    log_file.close()


def phone_number_check(): # Fuction to check valid numbers, ensures mobile prefixe's,
                          # is number digit, does mobile prefix's match and length of mobile number
    valid_numbers = """040, 041, 042, 043, 
                044, 045, 046, 049, 050"""

    try: 
        if phone_number is int(phone_number): 
            pass

        if phone_number[0:2] in valid_numbers and len(phone_number) == 10: 
            return f"Phone number +358{phone_number[1:9]} is valid"
        
        else:
            return "Number you gave is not a proper phone number in Finland"
    
    except ValueError:
        return "Number you gave is not a proper phone number in Finland VALUE ERROR"


def location(): # Client for geocoding web service. In this app Nominatim is used.
                # Ensures that end user is in chosen area, in this case Helsinki 
    geolocator = Nominatim(user_agent="application")
    location = geolocator.geocode(location_input)

    try:
        if "Helsinki" in location.address:
            return location.address 
            
        else:
            return "You're not in Helsinki"

    except AttributeError:
        return "Please, type address again.."


def email_check(): # Ensures email address is written in right form, doesn't check if email isValid
    pattern = re.compile(r"[a-zA-Z0-9]+.[a-zA-Z0-9]+@[a-z]+.[a-z]+")
    text_to_search = pattern.findall(string)     
    for text in text_to_search:
        return text
    

while True:
    string = input("Please, give your e-mail address: ")
    if email_check() == None:
        print("?")
    
    else:    
        print(email_check())
        break

while True:  
    phone_number = input("Please, give your phone number: ").replace(" ", "")
    
    if "is valid" in phone_number_check():
        print(phone_number_check())
        break
    
    else:
        print(phone_number_check())

while True:
    try:
        delivery_time_input = input("Do you want to have a specific delivery time (HH:mm)? ").replace(":","").replace(" ", "")
        print("Your delivery time is:", delivery_time())
        print(delivery_time_input)
        print("Time is now:", time_now())
        break
    
    except ValueError:
        print("Wrong time format, set time ie. '15:45'")
    
delivery_time()
    

make_dir() 


while True:
        location_input = input("Please, give your address: ")
        try:
            if "Uusimaa" in location() and "Helsinki" in location():
                print(location_input.capitalize())
                print(location())
                
            if "again" in location() or "not in" in location():
                print(location())
            
            else:
                try:
                    location_proof = input("Is this correct? Y/n ")
                    for a in location_proof:
                        if location_proof == "y" or location_proof == "Y":
                            location_logfile()
                            print("Adress saved.")
                            quit()

                        else:
                            location()

                except ValueError:
                    pass
        
        except ValueError:
            pass
