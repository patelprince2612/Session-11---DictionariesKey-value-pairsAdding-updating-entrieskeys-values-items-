# Task 1: Create a dictionary called my_playlist with three songs as keys and their durations in minutes as values, then print the dictionary.
my_playlist = {
    "Bohemian Rhapsody": 5.9,
    "Stairway to Heaven": 8.0,
    "Hotel California": 6.5
}
print(my_playlist)

# Task 2: Add a new song and its duration to your my_playlist dictionary, then update the duration of one existing song.
my_playlist["Shape of You"] = 3.9  
my_playlist["Bohemian Rhapsody"] = 6.0  
print(my_playlist)

# Task 3: Write a function display_friends() that takes a dictionary of Instagram usernames as keys and their follower counts as values, and prints each username with their followers in the format: 'username: 2.3K followers'.
def display_friends(instagram_accounts):
    for username, followers in instagram_accounts.items():
        print(f"{username}: {followers} followers")

accounts = {"@alice": "2.3K", "@bob_smith": "850", "@charlie_x": "1.1M"}
display_friends(accounts)

# Task 4: Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, use the keys(), values(), and items() methods to print: a) all food items, b) all quantities, and c) each item with its quantity.
food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}
print(list(food_order.keys()))
print(list(food_order.values()))
for item, qty in food_order.items():
    print(f"{item}: {qty}")

# Task 5: Build a function update_cart(cart, item, qty) that adds a new item to a Flipkart-style cart dictionary or updates the quantity if the item already exists, then returns the updated cart.
def update_cart(cart, item, qty):
    cart[item] = qty
    return cart

shopping_cart = {"Wireless Mouse": 1, "Keyboard": 1}
update_cart(shopping_cart, "Wireless Mouse", 2)
update_cart(shopping_cart, "Monitor", 1)
print(shopping_cart)