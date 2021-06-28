OWNERS = [
    {
      "id": 1,
      "name": "Skip",
      "phoneNumber": "615-555-1234"
    },
    {
      "id": 2,
      "name": "Chip",
      "phoneNumber": "615-555-4321"
    },
    {
      "id": 3,
      "name": "Flip",
      "phoneNumber": "615-867-5309"
    },
    {
      "id": 4,
      "name": "GracieLou Freebush",
      "phoneNumber": "615-945-0987"
    },
    {
      "name": "Harold",
      "phoneNumber": "931-777-9933",
      "id": 5
    }
  ]


def get_all_owners():
    return OWNERS

# Function with a single parameter
def get_single_owner(id):
    # Variable to hold the found owner, if it exists
    requested_owner = None

    # Iterate the owners list above. Very similar to the
    # for..of loops you used in JavaScript.
    for owner in OWNERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if owner["id"] == id:
            requested_owner = owner

    return requested_owner
def create_owner(owner):
    # Get the id value of the last owner in the list
    max_id = OWNERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the owner dictionary
    owner["id"] = new_id

    # Add the owner dictionary to the list
    OWNERS.append(owner)

    # Return the dictionary with `id` property added
    return owner