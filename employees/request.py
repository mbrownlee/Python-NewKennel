EMPLOYEES = [
    {
      "id": 1,
      "name": "Buffy",
      "specialty": "Teaching to heel",
      "locationId": 3
    },
    {
      "id": 2,
      "name": "Muffy",
      "specialty": "Trimming nails",
      "locationId": 3
    },
    {
      "id": 3,
      "name": "Clyde",
      "specialty": "Reading pet auras",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Sky",
      "specialty": "Coaxing out shy ones",
      "locationId": 1
    }
  ]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
