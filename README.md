# zootopia_api

data_fetcher.py:

It contains a function fetch_data(animal_name) that fetches data about animals from an API based on the given animal_name.
The function sends a GET request to the API endpoint https://api.api-ninjas.com/v1/animals with the animal_name as a query parameter.
The API requires an API key for authentication, and the key is stored in the API_KEY variable.
The response from the API is in JSON format and is returned as a list of animal dictionaries.

animals_web_generator.py:

It imports the data_fetcher module, which provides the fetch_data function.
The script defines several utility functions for generating and manipulating HTML and files.
The main function main() is responsible for generating an HTML page based on user input.
The user is prompted to enter the name of an animal.
The script then calls the fetch_data function from the data_fetcher module to retrieve animal data based on the user's input.
The retrieved data is serialized and transformed into a string representation suitable for an HTML page.
An HTML template file named animals_template.html is read, and a placeholder __REPLACE_ANIMALS_INFO__ is replaced with the serialized animal data.
If no data is retrieved for the specified animal, an appropriate message is generated.
The modified HTML content is written to a file named animal.html.
A success message is printed to the console.
In summary, the code fetches animal data from an API based on user input, serializes the data, and generates an HTML page using a template. The generated HTML page provides information about the queried animal or displays a message if the animal does not exist.
