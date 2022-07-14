# Import the necessary libraries for reading csv files
import csv
    next(data, None)
#print(data)

# Set the path for the csv file
with open("../resources/pokemon.csv") as pokemon_file:
    data = csv.reader(pokemon_file, delimiter = ",")
     next(data, None)
# Create new lists to store data for heaviest and tallest pokemon
heaviest = []
tallest = []
# Open the csv


    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.



        # Print the name of the pokemon(identifier) and pokedex number(species id) at that number. For example, "Pokemon No. 25 - pikachu".


        # Iterate through the data and search for pokemon whose weight is greater than 3000. Append only the pokemon's name and weight to the 'heaviest' list.


        # Iterate through the data and search for pokemon whose height is greater than 50. Append only the pokemon's name and height to the 'tallest' list.


# Print the list of heaviest and tallest pokemon

