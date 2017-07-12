
class UserInput:
    """
    Creates UserInput object.
    """

    def get_option(self, options):
        """
        Returns the option from the options list depending on the user input.
        Parameters:
        options: list

        Returns:
        user_decision: str
        """

        user_input_number = input("\nPick an option (number): ")
        while not user_input_number.isnumeric() or int(user_input_number) not in range(1, len(options) + 1):
            user_input_number = input("\nPick an PROPER option (number): ")
        user_decision = options[int(user_input_number) - 1]
        return user_decision

    def get_anykey(self):
        """
        Returns input that waits for anykey.
        """
        return input('Press --> ENTER<-- to move forward.')
