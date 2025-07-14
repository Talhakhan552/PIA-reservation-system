#-----------------------------------------
# This is the main file of the project.
#   But you can add as many files as you want.
#-----------------------------------------

#################################
# PIA reservation

import tkinter as tk
from tkinter import font
from tkinter import Frame
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


class Plane:
    def __init__(self):
        self.reservations = []
        self.reserved_seats = {       
            'Business': {},
            'Economy': {},
            'Student': {},
        }
        
        self.seat_widgets = {
            'Business': {},
            'Economy': {},
            'Student': {},
        }
        
        
        self.total_cargo = 0

        

    def add_seat_to_plane(self, seat_data):
        self.seat_name = seat_data["name"]
        self.seat_number = seat_data['seat_number']
        self.seat_class = seat_data['seat_class']
        self.cargo = float(seat_data["luggage_weight"]) 
        self.passenger_idd = seat_data["id"]
        
        
        self.reservations.append(seat_data)
        self.reserved_seats[self.seat_class][self.seat_number] = True
    
            
        for widget in self.seat_widgets[self.seat_class].values():
            if widget.cget('text') == self.seat_number:
                widget.configure(bg='green')
            

        print("Reservation added to the plane:", seat_data)
        
        
        return self.seat_name,self.seat_number,self.cargo
        
    
    def remove_seat_from_plane(self, seat_data):
        seat_number = seat_data['seat_number']
        seat_class = seat_data['seat_class']
        cargo = float(seat_data["luggage_weight"])

        self.reservations.remove(seat_data)
        del self.reserved_seats[seat_class][seat_number]

        for widget in self.seat_widgets[seat_class].values():
            if widget.cget('text') == seat_number:
                widget.configure(bg='silver')

        print("Reservation removed from the plane:", seat_data)
        return cargo


            
            
        
class PIAmanagement(Plane):
    
    def __init__(self):
        super().__init__() 
        self.window = tk.Tk()
        self.window.config(bg="silver")
        self.window.title("PIA Airline Reservation")
        self.window.geometry("600x400")
        
        self.seating_plan = tk.Toplevel()
        self.seating_plan.title("Seating Plan")
        self.seating_plan.geometry("300x850")
        
        
        self.reservation_dict = {}
        self.passenger_mapping = {}
        
        self.mainwindow()
        self.plane_window()
        
        
        
    def add_name_to_listbox(self, seat_class, seat_name):
        if seat_class == 'Business' :
            self.busi_box.insert(tk.END, seat_name)
        elif seat_class == 'Economy':
            self.econ_box.insert(tk.END, seat_name)
            
        elif seat_class == 'Student':
            self.stu_box.insert(tk.END, seat_name)



    
    def remove_name_from_listbox(self, seat_class, seat_name):
        if seat_class == 'Business':
            self.busi_box.delete(self.busi_box.get(0, tk.END).index(seat_name))
        elif seat_class == 'Economy':
            self.econ_box.delete(self.econ_box.get(0, tk.END).index(seat_name))
        elif seat_class == 'Student':
            self.stu_box.delete(self.stu_box.get(0, tk.END).index(seat_name))

    def call_reserve_seat(self):
        
        
        self.reserve_seat = tk.Tk()
        self.reserve_seat.config(bg="silver")
        self.reserve_seat.title("Reserve a seat")
        self.reserve_seat.geometry("300x200")

        self.name_label = tk.Label(self.reserve_seat, text="Name:", bg="silver")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.reserve_seat, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        self.id_label = tk.Label(self.reserve_seat, text="ID:", bg="silver")
        self.id_label.grid(row=1, column=0)
        self.id_entry = tk.Entry(self.reserve_seat, width=25)
        self.id_entry.grid(row=1, column=1)

        self.seat_class_label = tk.Label(self.reserve_seat, text="Seat Class:", bg="silver")
        self.seat_class_label.grid(row=2, column=0)
        self.seat_entry = tk.Spinbox(self.reserve_seat, values=("Business", "Economy", "Student"), width=20)
        self.seat_entry.grid(row=2, column=1)

        self.seat_num_label = tk.Label(self.reserve_seat, text="Seat Number:", bg="silver")
        self.seat_num_label.grid(row=3, column=0)
        self.seatnum_entry = tk.Entry(self.reserve_seat, width=25)
        self.seatnum_entry.grid(row=3, column=1)

        self.lugg_label = tk.Label(self.reserve_seat, text="Luggage Weight:", bg="silver")
        self.lugg_label.grid(row=4, column=0)
        self.lugg_entry = tk.Entry(self.reserve_seat, width=25)
        self.lugg_entry.grid(row=4, column=1)

        self.reserve_button = tk.Button(self.reserve_seat, text="Reserve", bg="silver", fg="Black", width=10, command=(self.reserve_seat_action)  )
        self.reserve_button.grid(row=6, column=0, pady=15)




        self.reserve_seat.mainloop()
        
        
    def info_under_plane(self):
        pass
        
    def reserve_seat_action(self):
        self.save_reservation()
        self.add_seat_to_plane(self.reservation_dict)  
        
        luggage_weight = float(self.reservation_dict['luggage_weight'])
        if luggage_weight > 100:
            messagebox.showerror("Error", "Luggage weight exceeds the limit of 100 kg per person.")
            return
        
        
        # self.seat_name, self.seat_number, self.cargo = self.add_seat_to_plane(self.reservation_dict)
        
        
        
        self.add_name_to_listbox(self.reservation_dict['seat_class'], self.reservation_dict['name'])
        self.total_cargo += self.cargo 
       
        
        total_passengers = len(self.reservations)
        self.total_passeenger_label.config(text=f"Total passengers: {total_passengers}")
        
        
        cargo_percentage = (self.total_cargo / 2000) * 100
        self.total_cargo_label.config(text=f"Total cargo: {cargo_percentage:.2f}%")
        
        
        
    def save_reservation(self):
        self.reservation_dict = {
            'name': self.name_entry.get(),
            'id': self.id_entry.get(),
            'seat_class': self.seat_entry.get(),
            'seat_number': self.seatnum_entry.get(),
            'luggage_weight': self.lugg_entry.get()
        }
        
        

        
    def call_cancel(self):
        
        self.cancel_win = tk.Toplevel()
        self.cancel_win.title("Cancel a seat")
        self.cancel_win.geometry("400x200")
        self.cancel_win.config(bg="silver")

        id = tk.Label(self.cancel_win, text="ID:",bg="silver")
        id.grid(row=1,column=0)
        id_entry = tk.Entry(self.cancel_win, width=30)
        id_entry.grid(row=1,column=1,padx=25)

    
        reserve_button = tk.Button(self.cancel_win, text="Cancel Seat", bg="silver", fg="Black", width=10, command=self.cancel_seat_action)
        reserve_button.grid(row=6, column=0, pady=15)

        self.cancel_win.mainloop()

    
    
    def call_savefile(self):
        save_file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file" ,".txt"),("HTML file", ".html"), ("All files", ".*")])
        
        
        
    # def call_loadfile(self):
    #     clear_terr = {}
    #     load_file = filedialog.askopenfilename()
    #     file = open(load_file, 'r+')

    #     count = int(file.readline())
    #     for i in range(count):
    #         line = file.readline()
    #         print(line.split())
    
    
    #     file.close()
    def call_loadfile(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.load_file(filename)

    
    
    
    def load_file(self, filename):
        clear_terr = {}

        with open(filename, 'r') as file:
            count = int(file.readline().strip())
            for i in range(count):
                line = file.readline().strip()
                passenger_id, clearance_id = line.split()
                clear_terr[passenger_id] = clearance_id

        for reservation in self.reservations:
            passenger_id = reservation['id']
            if passenger_id in clear_terr:
                clearance_id = clear_terr[passenger_id]
                self.update_seat_status(reservation['seat_number'], clearance_id)
            else:
                self.update_seat_status(reservation['seat_number'],None)



    def update_seat_status(self, seat_number, passenger_id):
        found = False
        for seat_class, seats in self.seat_widgets.items():
            if seat_number in seats:
                found = True
                if seat_class == 'Business' and passenger_id == "Terrorist":
                    seats[seat_number].configure(bg='red')
                elif seat_class == 'Economy' and passenger_id == "Terrorist":
                    seats[seat_number].configure(bg='red')
                elif seat_class == 'Student' and passenger_id == "Terrorist":
                    seats[seat_number].configure(bg='red')
                else:
                    seats[seat_number].configure(bg='green')
                
                break

        if not found:
            for seats in self.seat_widgets.values():
                for widget in seats.values():
                    if widget.cget('text') == seat_number:
                        widget.configure(bg='orange')
                        return
                    
                    

    def cancel_seat_action(self):
        reservation_to_cancel = None

        for reservation in self.reservations:
            if reservation['id'] == self.passenger_idd:
                reservation_to_cancel = reservation
                break
            
            
        if reservation_to_cancel:
            self.total_cargo -= self.remove_seat_from_plane(reservation_to_cancel)
            self.remove_name_from_listbox(reservation_to_cancel['seat_class'], reservation_to_cancel['name'])


            
            
            total_passengers = len(self.reservations)
            self.total_passeenger_label.config(text=f"Total passengers: {total_passengers}")
            
            
            cargo_percentage = (self.total_cargo / 2000) * 100
            self.total_cargo_label.config(text=f"Total cargo: {cargo_percentage:.2f}%")

            messagebox.showinfo("Success", "Reservation canceled successfully.")
            
            
        else:
            messagebox.showerror("Error", "No reservation found with the given ID.")

        
        # self.cancel_win.mainloop()

# ===================================================

    def mainwindow(self):

        frame1 = Frame(self.window,bg="silver")
        self.label_font = font.Font(size=15)
        self.label = tk.Label(frame1, text="PIA Ticket Reservation", width=50, font=self.label_font,bg="silver")
        self.label.pack()

        self.reservation_button = tk.Button(frame1, text="Seat Reservation", fg="black",bg="silver",command=self.call_reserve_seat)
        self.reservation_button.pack()

        self.cancellation_button = tk.Button(frame1, text="Seat Cancellation", fg="black",bg="silver", command=self.call_cancel)
        self.cancellation_button.pack()

        self.line_label = tk.Label(frame1, text="-------------------",bg="silver")
        self.line_label.pack()

        self.loadfile_button = tk.Button(frame1, text="Load from File", fg="black",bg="silver", command=self.call_loadfile)
        self.loadfile_button.pack()

        self.savefile_button = tk.Button(frame1, text="Save to files", fg="black",bg="silver", command=self.call_savefile)
        self.savefile_button.pack()

        frame1.pack()



        frame2 =Frame(self.window,bg="silver")

        self.font_size = font.Font(frame2, size=10)
        self.business_label = tk.Label(frame2, text="Business class", fg="Blue",bg="silver", font=self.font_size,padx=15)
        self.business_label.grid(row=7,column=0)

        self.font_size = font.Font(frame2, size=10)
        self.econ_label = tk.Label(frame2, text="Economy class", fg="Blue",bg="silver", font=self.font_size,padx=15)
        self.econ_label.grid(row=7,column=1)

        self.font_size = font.Font(frame2, size=10)
        self.stu_label = tk.Label(frame2, text="Student class", fg="Blue",bg="silver", font=self.font_size,padx=15)
        self.stu_label.grid(row=7,column=2)



        frame2.pack()
        frame2 =Frame(self.window,bg="silver")

        self.busi_box = tk.Listbox(frame2)
        self.busi_box.grid(row=8,column=0)

        self.econ_box = tk.Listbox(frame2)
        self.econ_box.grid(row=8,column=1)

        self.stu_box = tk.Listbox(frame2)
        self.stu_box.grid(row=8,column=2)
        
        frame2.pack()

# # ===========================================

# seating Plan
    def plane_window(self):

        plane_font = font.Font(self.seating_plan, size=20)
        plane_label = tk.Label(self.seating_plan, text="Plane # 1", bg='silver', font=plane_font)
        plane_label.grid(row=0,column=1,padx=50)

        busi_font = font.Font(self.seating_plan, size=10)
        business_label = tk.Label(self.seating_plan, text="Business class", fg="black",bg="lightgreen", font=busi_font)
        business_label.grid(row=1,column=1)


        busi_frame = Frame(self.seating_plan)
        business_seat = 1
        for i in range(3):
            for j in range(4):
                frame = tk.Frame(
                    master=busi_frame,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                Lable_buttons = tk.Label(master=frame, text=f"{business_seat}", width=5, height=2, bg="silver")
                Lable_buttons.pack()
                self.seat_widgets['Business'][business_seat] = Lable_buttons
                business_seat += 1
                
                
        busi_frame.grid(row=2,column=1)

        econ_font = font.Font(self.seating_plan, size=10)
        econ_label = tk.Label(self.seating_plan, text="Economy class", fg="black",bg="lightgreen", font=econ_font)
        econ_label.grid(row=3,column=1)


        econ_frame = Frame(self.seating_plan)
        economy_seat = 1
        for i in range(6):
            for j in range(4):
                frame = tk.Frame(
                    master=econ_frame,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                Lable_buttons = tk.Label(master=frame, text=f"{economy_seat}", width=5, height=2, bg="silver")
                Lable_buttons.pack()
                self.seat_widgets['Economy'][economy_seat] = Lable_buttons
                economy_seat += 1
                
        econ_frame.grid(row=4,column=1)

        stu_font = font.Font(self.seating_plan, size=10)
        stu_label = tk.Label(self.seating_plan, text="Student class", fg="black",bg="lightgreen", font=stu_font)
        stu_label.grid(row=5,column=1)

        stu_frame = Frame(self.seating_plan)
        student_seat = 1
        for i in range(2):
            for j in range(4):
                frame = tk.Frame(
                    master=stu_frame,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                Lable_buttons = tk.Label(master=frame, text=f"{student_seat}", width=5, height=2,bg="silver")
                Lable_buttons.pack()
                self.seat_widgets['Student'][student_seat] = Lable_buttons
                student_seat += 1
        stu_frame.grid(row=6,column=1)


        frame_info = Frame(self.seating_plan)
        self.total_passeenger_label = tk.Label(frame_info , text=f"Total passenger: {len(self.reservations)}", bg="lightgreen")
        self.total_passeenger_label.grid(row=8,column=1)
        self.total_cargo_label = tk.Label(frame_info, text=f"Total cargo:{(self.total_cargo/2000)*100}", bg="lightgreen")
        self.total_cargo_label.grid(row=9,column=1)
        self.total_revenue_label = tk.Label(frame_info , text=f"Toral Revenue", bg="lightgreen")
        self.total_revenue_label.grid(row=10,column=1)
        
        frame_info.grid(row=8,column=1)
    
PIAmanagement().window.mainloop()
    
            










# ===================================

# class PIAManagement:
#     def _init_(self,plane):
#         self.plane = plane
#         pass
    
# class Plane:
#     def _init_(self,passengers):
#         self,passengers = passengers


# class SeatingClass:
#     def _init_(self,seats):
#         self.seats = seats
#         pass
    
# class Seat:
#     def _init_(self) :
#         pass
    
# class Passenger:
#     def _init_(self):