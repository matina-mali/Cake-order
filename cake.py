class Cake:
    def _init_(self, name, price): #initialize name and price
        self.name = name
        self.price = price
    class Order:
        def _init_(self): #initialize order with empty list
            self.items = []
        def add_item(self, cake):
            self.items.append(coffee)
            print(f"Added {cake.name} to your order.")
        def total(self):
            return sum(item.price for item in self.items)
        def show_order(self):
            if not self.items:
                print("No items in order.")
                return
            print("\nYour order:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item.name}- ${item.price}")

            print(f"Total: Nrs {self.total()}")
            def checkout(self):
                if not self.items:
                    print("Cart is empty.")
                    return
                self>show_order()
                confirm = input("Proceed to checkout? (yes/no):").strip().lower
                if confirm == 'yes':
                    print("Order confirmed!")
                    self.items.clear()
                else:
                    print("Checkout cancelled.")
            def main(): #display menu and handle user input
                menu = [
                    Cake("vanilla",700),
                    Cake("strawberry", 800),
                    Cake("black forest", 770),
                    Cake("chocolate", 650),
                    Cake("cheesecake", 4400)
                ]
                order = Order()
                while True: #user interaction
                    print("\n-----Cake Menu-----")
                    for i, cake in enumerate(menu, 1):
                        print(f"{i}. {cake.name} - Nrs {cake.price}")
                    print("6. View Order")
                    print("7. Checkout")
                    print("8.Exit")
                    choice = input("Choose an option:")
                    if choicce in ['1', '2', '3', '4', '5']:
                        order.add_item(menu[int(choice) - 1])
                    elif choice == '6':
                        order.show_order()
                    elif choice == '7':
                        order.checkout()
                    elif choice == '8':
                        print("Thank you for visiting.")
                        break
                    else:
                        print("Invalid choice. Try again.")
            if _name_ == "_main_":
                main()



