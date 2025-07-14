# PIA-reservation-system

A Python 3 GUI application for managing PIA flight seat reservations, built with `tkinter`. It lets you reserve, cancel, and visualize seats in three classes—Business, Economy, and Student—while tracking cargo usage and revenue.

## Features

- **Object-Oriented Design**  
  Implements classes for management (`PIAManagement`), `Plane`, `SeatingClass`, `Seat`, and `Passenger` to keep logic modular and extensible :contentReference[oaicite:0]{index=0}.

- **Dual-Window Interface**  
  - **Main Control Panel**: reserve/cancel seats, load/save full state, view passenger lists per class :contentReference[oaicite:1]{index=1}.  
  - **Plane Seating View**: dynamically generated grid of disabled buttons shows seat status (gray = empty, green = clean passenger, red = terrorist, orange = unknown, yellow = selected) :contentReference[oaicite:2]{index=2}.

- **Passenger Data Integration**  
  Reads `isidata.txt` at startup to mark each seat according to citizen status (`CLEAN` or `TERRORIST`). Unlisted IDs appear as “unknown” :contentReference[oaicite:3]{index=3}.

- **Cargo & Revenue Tracking**  
  - Limits total luggage to 2 000 kg (100 kg per passenger).  
  - Calculates and displays total seats occupied, cargo percentage, and revenue based on class rates (Business ₹200 000, Economy ₹100 000, Student ₹40 000) :contentReference[oaicite:4]{index=4}.

- **Seat Reservation & Cancellation Dialogs**  
  Pop-up forms enforce:  
  - 7-digit numeric ID  
  - No duplicate reservations  
  - Appropriate error messages on invalid input or missing passenger :contentReference[oaicite:5]{index=5}.

- **Save & Load Functionality**  
  Persist entire application state (all planes, passengers, seating) to file and reload later :contentReference[oaicite:6]{index=6}.

- **Bonus (Optional)**  
  - Multiple-planes support with plane-selection combo box.  
  - Generic plane layout: specify seat counts and columns per class when adding a new plane.  
  - Early-submission bonus for fully functional code.

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/pia-seat-reservation.git
   cd pia-seat-reservation
