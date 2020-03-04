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

low_num = num_check("Enter a number between 1 and 10. ", 1, 10)
