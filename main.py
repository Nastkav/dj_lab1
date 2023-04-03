from tkinter import *
import pymysql

root = Tk()
root.geometry("500x500")


connection = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='shipping',
        )


cursor = connection.cursor()

flights = """CREATE TABLE flights (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        departure_location VARCHAR(255),
                        destination_location VARCHAR(255),
                        departure_date DATE,
                        arrival_date DATE,
                        ship_id INT,
                        FOREIGN KEY (ship_id) REFERENCES ships(id)
                        )"""
cursor.execute(flights)


ships = """CREATE TABLE ships (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        cargo_capacity FLOAT,
                        passengers_capacity INT,
                        available BIT
                        )"""
cursor.execute(ships)


tickets = """CREATE TABLE tickets (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        flight_id INT,
                        FOREIGN KEY (flight_id) REFERENCES flights(id),
                        price FLOAT,
                        available BIT
                        )"""
cursor.execute(tickets)

connection.commit()


class MainPanel:
    def __init__(self, master):
        self.master = master
        master.title("Main panel")

        self.create_button = Button(master, text="Create", command=self.create_flights)
        self.read_button = Button(master, text="Read", command=self.read_flights)

        self.create_button.grid(row=0, column=0, padx=10, pady=10)
        self.read_button.grid(row=0, column=1, padx=10, pady=10)


    def create_flights(self):
        create_window = Toplevel(self.master)
        create_window.title("Create Flights")

        Label(create_window, text="departure location:").grid(row=0, column=0)
        self.departure_location = Entry(create_window)
        self.departure_location.grid(row=0, column=1)

        Label(create_window, text="destination location :").grid(row=1, column=0)
        self.destination_location = Entry(create_window)
        self.destination_location.grid(row=1, column=1)

        Label(create_window, text="departure date:").grid(row=2, column=0)
        self.departure_date = Entry(create_window)
        self.departure_date.grid(row=2, column=1)

        Label(create_window, text="arrival date:").grid(row=3, column=0)
        self.arrival_date = Entry(create_window)
        self.arrival_date.grid(row=3, column=1)

        Label(create_window, text="id: ").grid(row=4, column=0)
        self.ship_id = Entry(create_window)
        self.ship_id.grid(row=4, column=1)


        add_button = Button(create_window, text="Add", command=self.add_record_flights)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)
    def read_flights(self):
        read_window = Toplevel(self.master)
        read_window.title("Flights")

        flights_listbox = Listbox(read_window, width=80)
        flights_listbox.grid(row=0, column=0, padx=10, pady=10)

        cursor.execute("SELECT * FROM flights")
        flights_data = cursor.fetchall()

        for flight in flights_data:
            flight_str = f"ID: {flight[0]}, Departure: {flight[1]}, Destination: {flight[2]}, " \
                         f"Departure Date: {flight[3]}, Arrival Date: {flight[4]}, Ship ID: {flight[5]}"
            flights_listbox.insert(END, flight_str)


panel = MainPanel(root)
root.mainloop()
connection.close()
