import data_fetcher

HTML_FILE_NAME = "animal.html"


def serialize_data_by_skin_type(data, skin_type):
    """
    Serializes the animal data for animals with the specified skin type.
    Returns a string of serialized animal data.
    """
    animals_data_as_list = []

    for animal in data:
        if animal.get("characteristics", {}).get("skin_type", "").lower() == skin_type:
            animals_data_as_list.append(serialize_animal(animal))

    return "\n".join(animals_data_as_list)


def get_user_input():
    """Get user input. return string"""
    user_input = input("Enter a name of an animal: ")
    return user_input


def get_skin_type_list(data):
    """Return list of animal skin types"""
    skin_types = set()
    for animal in data:
        skin_types.add(animal["characteristics"]["skin_type"])

    return list(skin_types)


def write_file(file_path, data):
    """Creates file_path with data"""
    with open(file_path, "w") as file:
        file.write(data)


def read_file(file_path):
    """Returns string data of file_path"""
    with open(file_path, "r") as file:
        return file.read()


def generating_empty_data_for_html(animal_name):
    output = ""
    output += '<li class="cards__item">'
    output += f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    output += '</li>'
    return output


def serialization_of_data_for_html(data, animal_name):
    """Serialization of data for html page. Returns string"""
    animals_data_as_string = ""
    if data:
        for animal in data:
            animals_data_as_string += serialize_animal(animal)
    else:
        animals_data_as_string = generating_empty_data_for_html(animal_name)

    return animals_data_as_string

def get_user_input():
    """Get user input. return string"""
    return input("Enter a name of an animal: ").strip()


def get_skin_type_set(data):
    """Return set of animal skin types"""
    skin_types = {animal["characteristics"]["skin_type"] for animal in data}
    return skin_types


def write_file(file_path, data):
    """Creates file_path with data"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)


def read_file(file_path):
    """Returns string data of file_path"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_empty_data_for_html(animal_name):
    return f'<li class="cards__item"><h2>The animal "{animal_name}" doesn\'t exist.</h2></li>'


def serialize_animal(animal):
    """Creates single animal serialization and returns it"""
    output = ""
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += "<p class='card__text'>\n"
    output += "<ul class='animal__card__list'>\n"
    output += f"<li><strong>Diet</strong>: {animal['characteristics']['diet']}</li>\n"
    output += f"<li><strong>Location</strong>: {animal['locations'][0]}</li>\n"
    if "type" in animal['characteristics']:
        output += f"<li><strong>Type</strong>: {animal['characteristics']['type']}</li>\n"
    output += "</ul>"
    output += "</p>\n"
    output += "</li>\n"

    return output

def main():
    """Generate html page by skin type that gets from user"""
    # get animal name from user
    animal_name_input = get_user_input()

    # getting data
    animals_data = data_fetcher.fetch_data(animal_name_input)

    animals_data_string_for_html = serialization_of_data_for_html(animals_data, animal_name_input)

    # creating animal1.html with serialized data
    html_page_data = read_file("animals_template.html")

    # check if animals_data is empty
    if not animals_data:
        animals_data_string_for_html = generating_empty_data_for_html(animal_name_input)

    html_page_data_reworked = html_page_data.replace(
        "__REPLACE_ANIMALS_INFO__", animals_data_string_for_html
    )
    write_file(HTML_FILE_NAME, html_page_data_reworked)

    print(f"Website was successfully generated to the file {HTML_FILE_NAME}")


if __name__ == '__main__':
    main()
