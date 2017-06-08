from flask import Flask

app = Flask(__name__)

#Main Restaurant page
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return "This page will show my restaurants"

#Create New Restaurant
@app.route('/restaurant/new')
def newRestaurant():
    return "This will be my new restaurant creating page"

#Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return "This is where you edit a restaurant %s" % restaurant_id

#Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "This is where you delete a restaurant %s" % restaurant_id

#Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return "This page is the menu for restaurant %s" % restaurant_id

#Create new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return "This is the the page for making new menu items for restaurant{}".format(restaurant_id)

#Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "This is the page to edit menu {} from restaurant {}".format(menu_id, restaurant_id)

#Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "This is the page to delete menu {} from restaurant {}".format(menu_id, restaurant_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
