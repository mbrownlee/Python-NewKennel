LOCATIONS = [
    {
      "id": 1,
      "area": "Nashville North",
      "address": "500 Puppy Way"
    },
    {
      "id": 2,
      "area": "Cool Springs",
      "address": "621 Pug Place"
    },
    {
      "area": "Spring Hill",
      "address": "468 Corgi Circle",
      "id": 3
    }
  ]


def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locations list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location
