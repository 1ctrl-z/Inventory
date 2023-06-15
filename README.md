# Inventory

This code represents a simple product inventory system for managing shoes. Here is a breakdown of the code:

Importing Libraries: The code begins by importing the tabulate library, which is used to display data in a tabular format.

Defining the Shoe class: The Shoe class is defined, representing a shoe object. It has attributes such as country, code, product, cost, and quantity. The __init__ method is the constructor function that initializes these attributes. The class also includes methods such as get_cost, get_quantity, set_quantity, and __str__ for retrieving and modifying the attribute values and displaying a string representation of the shoe object.

Shoe list: A list called shoe_list is created to store objects of shoes.

Functions outside the class: Several functions are defined outside the class to perform specific tasks:

read_shoes_data(): This function reads shoe data from a file called inventory.txt and creates shoe objects with the data, which are then appended to the shoe_list. It uses error handling with try-except blocks to handle potential errors while reading the file.

capture_shoes(): This function allows the user to input data about a shoe and creates a shoe object based on the input. The object is then appended to the shoe_list. It includes input validation and a menu to either add another shoe or return to the main menu.

view_all(): This function iterates over the shoe_list and prints the details of each shoe object using the __str__ method. It utilizes the tabulate module to display the data in a table format.

re_stock(): This function finds the shoe object with the lowest quantity in the shoe_list and offers the option to add more quantity. If chosen, the quantity is updated for that shoe object. It also writes the updated data to the file.

search_shoe(): This function allows the user to search for a shoe by its code and returns the corresponding shoe object if found.

value_per_item(): This function calculates the total value of each shoe item by multiplying the cost and quantity attributes of each shoe object. It then displays this information in a table format.

highest_qty(): This function finds the shoe with the highest quantity in the shoe_list and displays it as being for sale.

write_to_file(): This function writes the shoe objects in the shoe_list to the file inventory.txt in a specific format.

Main Menu: The code enters a while loop that presents a menu to the user and executes the corresponding functions based on their input. The menu is displayed until the user chooses to exit. The write_to_file function is called after each menu option to update the file with the latest data.

The provided code implements a basic shoe inventory system with functionalities such as capturing new shoes, viewing all shoes, restocking, searching by code, calculating value per item, finding the shoe with the highest quantity, and writing data to a file.




