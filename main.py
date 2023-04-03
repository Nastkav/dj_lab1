from tkinter import *
import mysql as mysql
import pymysql
import mysql.connector

# Connect to the database
try:
    connection = mysql.connector.connect(
        user='root',
        password='newpassword',
        host='127.0.0.1',
        database='shipping'
    )
    if connection.is_connected():
        print('Connected to MySQL database')
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")


cursor = connection.cursor()
# ships = """CREATE TABLE ships (
#                         id INT PRIMARY KEY AUTO_INCREMENT,
#                         name VARCHAR(255),
#                         cargo_capacity FLOAT,
#                         passengers_capacity INT,
#                         available BIT
#                         )"""
# try:
#     cursor.execute(ships)
# except:
#     print("Error executing ships table creation query.")
#
# flights = """CREATE TABLE flights (
#                         id INT PRIMARY KEY AUTO_INCREMENT,
#                         departure_location VARCHAR(255),
#                         destination_location VARCHAR(255),
#                         departure_date DATE,
#                         arrival_date DATE,
#                         ship_id INT,
#                         FOREIGN KEY (ship_id) REFERENCES ships(id)
#                         )"""
# try:
#     cursor.execute(flights)
# except:
#     print("Error executing flights table creation query.")
#
# tickets = """CREATE TABLE tickets (
#                         id INT PRIMARY KEY AUTO_INCREMENT,
#                         flight_id INT,
#                         FOREIGN KEY (flight_id) REFERENCES flights(id),
#                         price FLOAT,
#                         available BIT
#                         )"""
# try:
#     cursor.execute(tickets)
# except:
#     print("Error executing tickets table creation query.")
# # add data to ships table
#
# add_ships = "INSERT INTO ships (name, cargo_capacity, passengers_capacity, available) VALUES (%s, %s, %s, %s)"
# ships_data = [("Ship A", 100.0, 50, 1), ("Ship B", 200.0, 100, 1), ("Ship C", 300.0, 150, 0), ("Ship D", 400.0, 200, 1), ("Ship E", 500.0, 250, 0)]
# try:
#     cursor.executemany(add_ships, ships_data)
#     connection.commit()
#     print(cursor.rowcount, "record(s) inserted into ships table")
# except mysql.connector.Error as e:
#     print(f"Error inserting data into ships table: {e}")
#
# # add data to flights table
# add_flights = "INSERT INTO flights (departure_location, destination_location, departure_date, arrival_date, ship_id) VALUES (%s, %s, %s, %s, %s)"
# flights_data = [("A", "B", "2023-04-10", "2023-04-11", 1), ("B", "C", "2023-04-12", "2023-04-13", 2), ("C", "D", "2023-04-14", "2023-04-15", 3), ("D", "E", "2023-04-16", "2023-04-17", 4), ("E", "A", "2023-04-18", "2023-04-19", 5)]
# try:
#     cursor.executemany(add_flights, flights_data)
#     connection.commit()
#     print(cursor.rowcount, "record(s) inserted into flights table")
# except mysql.connector.Error as e:
#     print(f"Error inserting data into flights table: {e}")
#
# # add data to tickets table
# add_tickets = "INSERT INTO tickets (flight_id, price, available) VALUES (%s, %s, %s)"
# tickets_data = [(1, 100.0, 1), (2, 200.0, 1), (3, 300.0, 0), (4, 400.0, 1), (5, 500.0, 0)]
# try:
#     cursor.executemany(add_tickets, tickets_data)
#     connection.commit()
#     print(cursor.rowcount, "record(s) inserted into tickets table")
# except mysql.connector.Error as e:
#     print(f"Error inserting data into tickets table: {e}")

connection.commit()

root = Tk()
root.geometry("500x500")

class MainPanel:
    def __init__(self, master):
        self.master = master
        master.title("Main panel")

        self.create_button = Button(master, text="Create", command=self.create_flights)
        self.read_button = Button(master, text="Read", command=self.read_flights)
        self.update_button = Button(master, text="Update", command=self.update_flights)
        self.delete_button = Button(master, text="Delete", command=self.delete_flights)

        self.create_button.grid(row=0, column=0, padx=10, pady=10)
        self.read_button.grid(row=0, column=1, padx=10, pady=10)
        self.update_button.grid(row=0, column=2, padx=10, pady=10)
        self.delete_button.grid(row=0, column=3, padx=10, pady=10)


    def create_flights(self):
        create_window = Toplevel(self.master)
        create_window.title("Create Flights")

        Label(create_window, text="departure location: ").grid(row=0, column=0)
        self.departure_location = Entry(create_window)
        self.departure_location.grid(row=0, column=1)

        Label(create_window, text="destination location: ").grid(row=1, column=0)
        self.destination_location = Entry(create_window)
        self.destination_location.grid(row=1, column=1)

        Label(create_window, text="departure date: ").grid(row=2, column=0)
        self.departure_date = Entry(create_window)
        self.departure_date.grid(row=2, column=1)

        Label(create_window, text="arrival date: ").grid(row=3, column=0)
        self.arrival_date = Entry(create_window)
        self.arrival_date.grid(row=3, column=1)

        Label(create_window, text="ship id: ").grid(row=4, column=0)
        self.ship_id = Entry(create_window)
        self.ship_id.grid(row=4, column=1)

        add_button = Button(create_window, text="Add", command=self.add_record_flights)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_record_flights(self):
            departure_location = self.departure_location.get()
            destination_location = self.destination_location.get()
            departure_date = self.departure_date.get()
            arrival_date = self.arrival_date.get()
            ship_id = self.ship_id.get()

            add_flights = "INSERT INTO flights (departure_location, destination_location, departure_date, arrival_date, ship_id) VALUES (%s, %s, %s, %s, %s)"
            data = (departure_location, destination_location, departure_date, arrival_date, ship_id)

            try:
                cursor.execute(add_flights, data)
                connection.commit()
                print(cursor.rowcount, "record added")
            except mysql.connector.Error as e:
                print(f"Error adding record: {e}")

            self.departure_location.delete(0, END)
            self.destination_location.delete(0, END)
            self.departure_date.delete(0, END)
            self.arrival_date.delete(0, END)
            self.ship_id.delete(0, END)
            
            
    def read_flights(self):
        read_window = Toplevel(self.master)
        read_window.title("Flights")

        flights_listbox = Listbox(read_window, width=80)
        flights_listbox.grid(row=0, column=0, padx=10, pady=10)

        cursor.execute("SELECT * FROM flights")
        flights_data = cursor.fetchall()

        for flight in flights_data:
            flight_str = f"ID: {flight[0]}, Departure location: {flight[1]}, Destination  location: {flight[2]}, " \
                         f"Departure Date: {flight[3]}, Arrival Date: {flight[4]}, Ship ID: {flight[5]}"
            flights_listbox.insert(END, flight_str)

    def update_flights(self):
        update_window = Toplevel(self.master)
        update_window.title("Update Flights By ID")

        # Create widgets for input
        id_label = Label(update_window, text="Enter Flight ID:")
        id_entry = Entry(update_window)
        search_button = Button(update_window, text="Search", command=lambda: search_flight(id_entry.get()))

        id_label.grid(row=0, column=0, padx=10, pady=10)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        search_button.grid(row=0, column=2, padx=10, pady=10)

        # Create widgets for displaying and updating the selected record
        departure_label = Label(update_window, text="Departure Location:")
        destination_label = Label(update_window, text="Destination Location:")
        departure_date_label = Label(update_window, text="Departure Date:")
        arrival_date_label = Label(update_window, text="Arrival Date:")
        ship_id_label = Label(update_window, text="Ship ID:")

        departure_entry = Entry(update_window)
        destination_entry = Entry(update_window)
        departure_date_entry = Entry(update_window)
        arrival_date_entry = Entry(update_window)
        ship_id_entry = Entry(update_window)

        update_button = Button(update_window, text="Update", command=lambda: update_record(id_entry.get(),
                                                                                           departure_entry.get(),
                                                                                           destination_entry.get(),
                                                                                           departure_date_entry.get(),
                                                                                           arrival_date_entry.get(),
                                                                                           ship_id_entry.get()))

        departure_label.grid(row=1, column=0, padx=10, pady=10)
        destination_label.grid(row=2, column=0, padx=10, pady=10)
        departure_date_label.grid(row=3, column=0, padx=10, pady=10)
        arrival_date_label.grid(row=4, column=0, padx=10, pady=10)
        ship_id_label.grid(row=5, column=0, padx=10, pady=10)

        departure_entry.grid(row=1, column=1, padx=10, pady=10)
        destination_entry.grid(row=2, column=1, padx=10, pady=10)
        departure_date_entry.grid(row=3, column=1, padx=10, pady=10)
        arrival_date_entry.grid(row=4, column=1, padx=10, pady=10)
        ship_id_entry.grid(row=5, column=1, padx=10, pady=10)

        update_button.grid(row=6, column=1, padx=10, pady=10)

        def search_flight(flight_id):
            """Searches for a flight by ID and displays its data in the entry widgets"""
            query = f"SELECT * FROM flights WHERE id = {flight_id}"
            cursor.execute(query)
            flight_data = cursor.fetchone()

            if flight_data is not None:
                departure_entry.delete(0, END)
                departure_entry.insert(0, flight_data[1])

                destination_entry.delete(0, END)
                destination_entry.insert(0, flight_data[2])

                departure_date_entry.delete(0, END)
                departure_date_entry.insert(0, flight_data[3])

                arrival_date_entry.delete(0, END)
                arrival_date_entry.insert(0, flight_data[4])

                ship_id_entry.delete(0, END)
                ship_id_entry.insert(0, flight_data[5])

        def update_record(flight_id, departure, destination, departure_date, arrival_date, ship_id):
            """Updates a flight record with the given data"""


    def delete_flights(self):
        delete_window = Toplevel(self.master)
        delete_window.title("Delete Flights By ID")

panel = MainPanel(root)
root.mainloop()
connection.close()

