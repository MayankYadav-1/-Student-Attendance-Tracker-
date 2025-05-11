Student Attendance Tracker
The Student Attendance Tracker is a desktop application built entirely in Python, designed to help teachers or administrators efficiently manage and track student attendance. This project makes use of Tkinter for the graphical user interface (GUI), SQLite for database management, and CSV for exporting attendance records. The application provides a simple and user-friendly interface that allows for adding student records, marking attendance, viewing attendance logs, filtering attendance by date range, and exporting the data to CSV format for further reporting or storage.

Features:
Add Students: You can easily add students to the system by entering their name into the application. Each student is uniquely identified in the database.

Mark Attendance: Attendance can be recorded for each student by selecting their name, specifying their attendance status (Present or Absent), and providing the date in the format YYYY-MM-DD. The application will store the attendance in an SQLite database for later retrieval.

View Attendance Records: The application allows you to view all attendance records. A window is provided that lists all students' attendance along with the date and their status (Present/Absent).

Date-Based Filtering: Users can filter attendance records by providing a specific date range. The system will show attendance logs between the selected start and end dates.

Export to CSV: The application allows you to export the stored attendance data to a CSV file. This is useful for sharing the attendance data with others, generating reports, or archiving records.

Technologies Used:
Python 3.x: The entire project is built using Python.

Tkinter: For creating the graphical user interface, allowing users to interact with the system.

SQLite: A lightweight, serverless database used to store student and attendance data locally.

CSV: Used to export the attendance data to CSV format for easy reporting and data sharing.

FileDialog and MessageBox: Tkinter modules that provide file selection dialogs and user feedback messages, respectively.

How to Run:
Clone or Download the Repository:

Clone the repository from GitHub or download the ZIP file of the project.

If cloning, use the following Git command:

bash
Copy
Edit
git clone https://github.com/yourusername/student-attendance-tracker.git
cd student-attendance-tracker
Install Python:

Ensure that Python 3.x is installed on your system. No additional Python libraries or packages are required, as the project uses only Python's built-in modules.

Run the Application:

Simply run the Python script attendance_tracker.py using the following command:

bash
Copy
Edit
python attendance_tracker.py
A graphical window will open, where you can interact with the application.

Instructions for Use:
Adding Students:

In the "Add Student" section, enter the student's name and click the "Add" button. The student will be added to the system and stored in the database.

Marking Attendance:

In the "Mark Attendance" section, select a student from the dropdown list.

Choose the attendance status (Present or Absent).

Enter the date in the format YYYY-MM-DD (e.g., 2025-05-11).

Click the "Mark" button to save the attendance record.

Viewing Attendance Records:

Click the "View Attendance Records" button to open a window displaying all attendance records, including the student's name, date, and attendance status.

Filtering Attendance by Date:

Enter the start date and end date in the format YYYY-MM-DD.

Click the "Filter" button to view only the attendance records within the specified date range.

Exporting Attendance to CSV:

Click the "Export to CSV" button to open a file dialog where you can choose the location to save the CSV file.

The CSV file will contain the student's name, attendance date, and status, and it can be opened in spreadsheet software for further analysis or reporting.

Acknowledgments:
Tkinter: A built-in Python library for creating graphical user interfaces.

SQLite: A simple and effective database management system that is perfect for small applications.

CSV module: For exporting attendance data to CSV files.

Python developers and contributors who created and maintained the libraries used in this project.

This project provides a simple yet effective solution for managing student attendance and can be expanded with additional features such as generating reports, sending reminders, or adding a login system for multiple users. It’s a great tool for those looking to practice database management, GUI design, and offline applications with Python.

Tips for Using the Project:
No dependencies: The project uses only Python's built-in libraries, so you don't need to install anything extra.

Offline Usage: It’s entirely offline — perfect for classroom environments where internet access may be limited.

Easily Extendable: You can add more features like generating reports, adding a login system, or integrating email notifications.
