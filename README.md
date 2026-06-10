# ToDo


This project is a simple yet functional To-Do List web application built using Python, Flask, HTML, and CSS. It allows users to create, view, manage, and delete daily tasks through an interactive web interface. The application was developed as a learning project to understand the fundamentals of Flask web development, routing, form handling, file operations, and template rendering.

The application provides a clean and user-friendly interface where users can add new tasks, view all existing tasks, delete individual tasks, or clear the entire task list. Tasks are stored persistently in a text file, ensuring that they remain available even after the application is restarted. This approach helps demonstrate how data persistence can be achieved without using a database.

One of the key features of this project is the integration of Flask with Jinja2 templates. Task data is dynamically passed from Python to HTML using the `render_template()` function, allowing the webpage to update automatically whenever tasks are added or removed. The project also displays the current date and a live digital clock using JavaScript, making the interface more interactive and user-friendly.

### Features

* Add new tasks through a web form
* View all saved tasks in a structured table
* Delete individual tasks
* Clear the complete task list with a single click
* Persistent task storage using a text file
* Dynamic content rendering using Flask and Jinja2
* Real-time clock display using JavaScript
* Responsive and clean user interface with HTML and CSS
* Font Awesome icons for enhanced visual appearance

### Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Jinja2 Templating Engine
* Font Awesome

### Learning Outcomes

This project helped in understanding:

* Flask application structure
* Route creation and request handling
* GET and POST methods
* Form data processing using `request`
* File handling in Python
* Dynamic webpage rendering using templates
* Basic frontend styling with CSS
* Integration of JavaScript into Flask applications

### Future Improvements

Some planned enhancements for future versions include:

* Replacing text-file storage with an SQLite or MySQL database
* User authentication and login system
* Task editing functionality
* Task priorities and categories
* Due dates and reminders
* Improved responsive design for mobile devices
* Search and filter functionality

This project serves as a strong beginner-friendly introduction to full-stack web development using Flask and demonstrates how backend logic, data storage, and frontend design work together to create a complete web application.
