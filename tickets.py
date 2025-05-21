# This application pre-sells cinema tickets.

class Tickets:
    def __init__(self):
        self.quantity = 20

    # Create a function to display the quantity of tickets available.
    def show_tickets(self):

        print('-----Welcome to the Movies-----')
        print('\n')
        print(f'There are {self.quantity} tickets available for purchase.')
        print('You can only purchase up to four tickets.')

    # Create a function to make the purchase
    def purchase_tickets(self, num_requested):
        if num_requested > 4:
            print('You can only purchase up to four tickets')
            return  False
        elif num_requested > self.quantity:
            print(f'Only {self.quantity} tickets are available.')
            return False
        elif num_requested <= 0:
            print('Please enter a positive number of tickets')
            return False
        else:
            self.quantity -= num_requested
            print(f'Purchase successful! {self.quantity} tickets remaining.')
            return True

ticket_system = Tickets()
ticket_system.show_tickets()


# Loop while there are still tickets
while ticket_system.quantity > 0:
    print("\n--- New Customer ---")
    try:
        requested = int(input("How many tickets would you like to buy? "))
        success = ticket_system.purchase_tickets(requested)
        if not success:
            continue  # retry current customer if input was invalid
        if ticket_system.quantity == 0:
            print("\nAll tickets are sold out!")
            break

        # Ask the user if they want to continue
        again = input("Would another customer like to buy tickets? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you! Enjoy the movie!")
            break

    except ValueError:
        print("Please enter a valid number.")