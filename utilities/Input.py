class Input:
    @staticmethod
    def get_input(input_type, message=None,):
        try:
            value = input_type(input()) if message is None else input_type(input(message))
            return value
        except ValueError:
            print(" Wrong type of value Entered, Enter again")
            return Input.get_input(input_type, message)