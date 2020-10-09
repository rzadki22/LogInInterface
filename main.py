from LogIn import *

user_1 = User("Jan", "Kowalski", "JaKow", "1234")
user_2 = User("Olaf", "Hartaard", "OlHa", "0000")

store = Store()
store.register(user_1)
store.register(user_2)
try:
    store.login("OlHa", "0001")
except:
    store.login("OlHa", "0000")

store.buy("Beer", 1)
store.buy("Cigarettes", 1)
store.buy("Candies", 2)
print(store)
store.logout

store.login("JaKow", "1234")
store.buy("Orange", 30)
store.buy("Banana", 10)
store.buy("Potato", 20)
print(store)
store.logout
