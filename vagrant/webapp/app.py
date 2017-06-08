#Main Restaurant page
@app.route('/')
@app.route('/restaurants/')

#Create New Restaurant
@app.route('/restaurant/new')

#Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')

#Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')

#Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>/menu/')

#Create new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new/')

#Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')

#Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
