def num_check(question, low, high):
    valid = False
    while not valid:
        error = "Please enter a number between {} and {}".format(low, high)
        print("")
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

# To do
# Check a lowest is an integer (any integer)
# Check that highest is more than lowest (lower bound only)