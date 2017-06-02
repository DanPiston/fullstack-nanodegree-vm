from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #Home page
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h3><a href='restaurants/new'>Click to Create New Restaurant</a></h3>"
                for restaurant in restaurants:
                    print restaurant.name
                    output += """
                        \n<h3>{}</h3>
                        \n<a href='/restaurants/{}/edit'>Edit</a>
                        \n<a href='/restaurants/{}/delete'>Delete</a>
                        """.format(restaurant.name, restaurant.id, restaurant.id)
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            #Create a new Restaurant page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += """
                        <form method = 'POST'
                        enctype='multipart/form-data'
                        action='/restaurants/new'>
                        <input name="new_restaurant" type = "text" placeholder="Name">
                        <input type="submit" value="Submit"></form>
                        """
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            #Delete page
            if self.path.endswith("/delete"):
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = "<html><body>"
                        output += "<h1>Are you sure you want to delete {}</h1>".format(myRestaurantQuery.name)
                        output += "<form method='POST' enctype='multipart/form-data' action ='/restaurants/{}/delete'>".format(restaurantIDPath)
                        output += "<input type = 'submit' value = 'Delete'>"
                        output += "</form>"
                        output += "</body></html>"
                        self.wfile.write(output)
            #Edit page
            if self.path.endswith("/edit"):
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = "<html><body>"
                        output += "<h1>{}</h1>".format(myRestaurantQuery.name)
                        output += "<form method='POST' enctype='multipart/form-data' action ='/restaurants/{}/edit'>".format(restaurantIDPath)
                        output += "<input name = 'new_restaurant' type='text' placeholder = '{}'>".format(myRestaurantQuery.name)
                        output += "<input type = 'submit' value = 'Rename'>"
                        output += "</form>"
                        output += "</body></html>"
                        self.wfile.write(output)


        except:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(
                        self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        session.delete(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                        self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('new_restaurant')
                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                        self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('new_restaurant')

                    #Create new restaurant
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()




        except:
            pass

    

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
