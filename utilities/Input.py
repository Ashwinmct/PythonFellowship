class Input:
    @staticmethod
    def get_input(message, input_type):
        try:
            value = input_type(input(message))
            return value
        except ValueError:
            print(" Wrong type of value Entered, Enter again")
            return Input.get_input(message, input_type)