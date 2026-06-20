# Q3 - Shopping Cart with Default & Mutable Pitfall

# ---------------------------------------------------------
# Part A - Spot the Bug
# ---------------------------------------------------------
# The buggy version is shown below as a comment, not run directly,
# so it doesn't interfere with the fixed version further down.
#
# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart
#
# print(add_item("apple"))
# print(add_item("banana"))
# print(add_item("milk", cart=["bread"]))
# print(add_item("eggs"))
#
# Predicted output:
# ["apple"]
# ["apple", "banana"]
# ["bread", "milk"]
# ["apple", "banana", "eggs"]
#
# Why this happens:
# Default argument values in Python are evaluated only ONCE, when the
# function is defined, not every time it's called. So cart=[] creates
# a single list object that is reused across every call where the
# caller does not pass their own cart. Each call that doesn't supply
# a cart keeps appending to that same shared list, which is why
# "apple" and "banana" both end up together, and then "eggs" gets
# added to that same list again even though it looks like a fresh call.


# ---------------------------------------------------------
# Part B - Fix It
# ---------------------------------------------------------
def add_item(item, cart=None):
    # use None as the default (immutable, safe) and create a new
    # list inside the function body if no cart was passed in
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# ---------------------------------------------------------
# Part C - Build the Cart
# ---------------------------------------------------------
def create_cart(owner, discount=0):
    # discount=0 is safe as a default because integers are immutable.
    # rebinding discount inside a function never affects the original 0.
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    # Tuples are immutable, so this line would raise a TypeError
    # if uncommented:
    #
    # price_tuple[0] = new_price
    #
    # Tuples don't support item assignment because their internal
    # storage is fixed at creation time. This is intentional -
    # tuples are meant to represent fixed records that shouldn't
    # change after being created.
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Cannot update tuple - {e}")


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]

    discount_amount = subtotal * (cart["discount"] / 100)
    final_total = subtotal - discount_amount
    return final_total


def main():
    # --- Test Part B fix ---
    print("Testing fixed add_item function:")
    print(add_item("apple"))
    print(add_item("banana"))
    print(add_item("milk", cart=["bread"]))
    print(add_item("eggs"))
    print()

    # --- Test Part C: two independent customers ---
    cart1 = create_cart("Ravi", discount=10)
    cart2 = create_cart("Meera")  # no discount, uses default 0

    add_to_cart(cart1, "Laptop Bag", 1200, qty=1)
    add_to_cart(cart1, "Notebook", 50, qty=3)

    add_to_cart(cart2, "Headphones", 800, qty=2)

    print("Cart 1 (Ravi):", cart1)
    print("Cart 2 (Meera):", cart2)
    print()

    # proves carts are independent - cart2 should NOT contain Ravi's items
    print("Cart 1 total:", calculate_total(cart1))
    print("Cart 2 total:", calculate_total(cart2))
    print()

    # --- Test update_price on a tuple ---
    price_info = (1200, "INR")
    update_price(list(price_info), 1100)  # works fine on a list
    update_price(price_info, 1100)        # fails, tuple is immutable


if __name__ == "__main__":
    main()


# ---------------------------------------------------------
# Discussion 
# ---------------------------------------------------------
# 1. Why is discount=0 safe but cart=[] dangerous?
#    Integers are immutable. Each time the function runs, discount
#    just refers to the same int object 0, and using it (e.g. in
#    a calculation) never modifies that object. A list, however,
#    is mutable, so calling .append() on the default list actually
#    changes the one shared object that gets reused on every call.
#
# 2. Difference between rebinding and mutating:
#    Rebinding means pointing a variable name to a new object,
#    e.g. x = x + [1] creates a new list and reassigns x to it.
#    Mutating means changing the object in place without creating
#    a new one, e.g. x.append(1) modifies the existing list directly.
#    Rebinding inside a function does not affect the caller's
#    variable, but mutating a mutable object does, since both the
#    caller and the function are pointing to the same object in memory.
#
# 3. Which of these are mutable - list, tuple, dict, set, str, int?
#    Mutable: list, dict, set
#    Immutable: tuple, str, int
#
# 4. When you pass a list into a function and modify it, do changes
#    reflect outside? Why?
#    Yes. Python passes object references, not copies. So the
#    parameter inside the function and the variable outside the
#    function both point to the same list object in memory.
#    Mutating it (append, remove, etc.) changes the one shared
#    object, so the change is visible outside the function too.
#    Reassigning the parameter to a brand new list, however, would
#    NOT affect the caller, since that just rebinds the local name.
