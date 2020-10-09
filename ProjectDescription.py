"""
Napiszcie klasy
class User:
  your code
class Store:
  def login()
  def logout()
  @is_logged_in
  def buy()
  
1. case
user = User()
store = Store()
store.register(user)
store.login
store.buy() --> success

2. case
user = User()
store = Store()
store.buy() --> You must be logged in!

3. case
user = User()
store = Store()
store.register(user)
store.buy() --> You must be logged in!

4. case
user = User()
store = Store()
store.login(user) --> No such account!

Czyli klasę Store, klasę User i chciałbym, aby User mógł się zalogować do 
serwisu, a najpierw zarejestrować i przy metodach w których kupujemy, albo 
przeglądamy jakieś artykuły to tam chcielibyśmy tylko zalogowanych 
użytkowników i to sprawdzajcie dekoratorem (edited) 

3:54
Oczywiście klas może być więcej i możecie to dowolnie rozbudować, ale fajnie 
jakby każdy zrobił przynajmniej tą imitację rejestracji i logowania!
"""