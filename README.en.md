# Taxi — Design and Implementation of a Taxi Database (MySQL) with a PyQt6 Client Application

[![Русский](https://img.shields.io/badge/🌐_Язык-Русский-red?style=for-the-badge)](README.md)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)
![MySQL Workbench](https://img.shields.io/badge/MySQL%20Workbench-modeling-orange)

Course project for the "Databases" discipline, Don State Technical University (DSTU), 2024.
Topic: **"Design and implementation of the Taxi database"**.

## About the Project

The core of the work is the **design and implementation of a relational database for a taxi service** in MySQL: from domain analysis and the ER model to normalization, the physical schema, stored procedures and audit triggers. To show the database in action, a desktop application in Python (PyQt6) was written on top of it, with three roles: **client**, **driver** and **administrator**.

### What Was Done

- analyzed the domain and identified three user roles and 11 entities;
- built an ER diagram, described the relationships and functional dependencies;
- normalized the relations to **third normal form (3NF)**;
- created the datalogical schema and implemented the database in **MySQL** (11 tables, primary and foreign keys, constraints);
- wrote **stored procedures** for all write operations (registration, login, orders, chats, feedback, services);
- created **triggers** that save a copy of a record to an audit log in JSON format before every data change;
- implemented a client interface that works with the database through procedures and parameterized queries.

## Database Design

### Users and Their Tasks

| Role | What it does with the data |
| ---- | -------------------------- |
| **Client** | Creates an order, chats with the driver and support, leaves feedback with a rating, views the order and feedback history |
| **Driver** | Views and accepts active orders, chats with the client, completes the order, records car maintenance data, views order history and feedback |
| **Administrator** | Has all of the driver's rights, and also manages employees, clients, cars, services and feedback, and answers in the support chat |

Eleven entities were identified from the requirements: **employee, client, car, work shift, order, feedback, chat, message, service, rendered service, medical check**.

### ER Diagram

![ER diagram](image/er_diagram.png)

Relationship types (all are one-to-many except order and feedback):

| Relationship | Type | Meaning |
| ------------ | ---- | ------- |
| `client` → `order_client` | 1 : N | A client makes many orders |
| `work_shift` → `order_client` | 1 : N | Many orders are served during a shift |
| `order_client` → `feedback` | 1 : 1 | An order has one feedback |
| `worker` → `work_shift` | 1 : N | An employee has many shifts |
| `car` → `work_shift` | 1 : N | A car works in different shifts |
| `client` → `chat`, `worker` → `chat` | 1 : N | A client and an employee can have many chats |
| `chat` → `message` | 1 : N | A chat has many messages |
| `worker` → `medical` | 1 : N | An employee has many medical checks |
| `car` → `service_rendered`, `service` → `service_rendered` | 1 : N | A service is performed on a car |

### Normalization

1. **1NF.** All attributes are atomic; values are not lists.
2. **2NF.** Every relation has a simple (non-composite) primary key, so non-key attributes depend fully on the key.
3. **3NF.** Transitive dependencies were eliminated by decomposition: employee and client data are placed in separate relations.

Result: minimal logical redundancy and a lower chance of insertion, update and deletion anomalies.

### Datalogical Schema

![Datalogical schema](image/datalogical_schema.png)

## Physical Implementation in MySQL

### Why MySQL

Oracle Database, MS SQL Server, PostgreSQL and MySQL were considered. **MySQL** was chosen: it is free, cross-platform, reliable and fast, has good Python support (`mysql-connector-python`), and its modeling and administration are convenient in MySQL Workbench.

### Table Schema

| Table | Purpose |
| ----- | ------- |
| `client` | Clients: phone number and login password |
| `worker` | Employees (drivers and administrators): full name, phone, position, activity flag |
| `car` | Cars: license plate (key), model, color |
| `work_shift` | Work shifts: employee, car, date, state |
| `order_client` | Orders: client, shift, addresses, price, distance, time, state |
| `feedback` | Client feedback on orders: rating (1–5) and text |
| `chat`, `message` | Chats between a client and an employee (including support) and their messages |
| `medical` | Drivers' medical conclusions before a shift |
| `service`, `service_rendered` | Service catalog and records of car maintenance |
| `audit_log` | Change log filled by triggers |

**What ensures data integrity:**

- primary keys in all tables (`AUTO_INCREMENT` for numeric ones, the license plate for `car`, the name for `service`);
- foreign keys (`FOREIGN KEY`) between all related tables, 13 relationships in total;
- `NOT NULL` for mandatory attributes, `UNIQUE` for the employee's phone, and the default value `'Да'` ("yes") for the activity flag;
- the uniqueness of a client's phone is checked in the `register_client` procedure;
- `utf8mb4` encoding, `InnoDB` engine.

![Table creation script example](image/sql_create_table.png)

### Stored Procedures

All write operations and the login are performed **through stored procedures**: the data-handling logic lives in the database, and the application only calls them via `cursor.callproc(...)`.

| Procedure | What it does |
| --------- | ------------ |
| `check_client` | Checks whether a client with this phone and password is registered, returns a boolean |
| `log_in` | Authentication by phone and password: returns a success flag and the position (client, driver or administrator) |
| `register_client` | Registers a new client if the number is not taken yet, otherwise returns `FALSE` |
| `creating_order` | Creates an order in `order_client` and returns its identifier |
| `update_order` | Updates an order: state, shift, time and distance (called as `update_order_worker` in the application code) |
| `update_order_state` | Changes the order state |
| `get_worker_and_car_info` | Returns the driver and car data for a shift: full name, model, color |
| `insert_chat`, `update_chat_status` | Creating a chat and changing its status (`Активен` / `Закрыт`, "active" / "closed") |
| `insert_message` | Adding a message to a chat |
| `insert_feedback` | Adding feedback with a rating |
| `insert_service_rendered` | Recording car maintenance |

![Stored procedure example](image/sql_procedure.png)

### Triggers and the Audit Log

For the `car`, `chat`, `feedback`, `medical`, `message`, `order_client`, `service`, `service_rendered`, `work_shift` and `worker` tables, three triggers each were created: `BEFORE INSERT`, `BEFORE UPDATE` and `BEFORE DELETE`. Before every operation, the trigger writes the operation time, table name, action type and the record data in **JSON** format (`old_data` / `new_data`) into the `audit_log` table. This gives a full change history and makes it possible to roll back or restore data.

An additional business rule: before a shift number is inserted into an order, the shift is checked for active orders, so a driver cannot perform two orders at the same time.

![Trigger example](image/sql_trigger.png)

## How the Application Works with the Database

- **Connection.** The connection parameters (`host`, `user`, `password`, `db_name`) are kept in `config.py`; the connection is opened via `mysql.connector`.
- **Writes** go through stored procedures, and **reads** use `SELECT` with **parameterized queries** (`%s`), which protects against SQL injection.
- **Roles** are determined at login: the `log_in` procedure returns the position, and the application opens the client, driver or administrator window.
- **Near-real-time updates.** The order waiting and accepted-order windows of the client and the driver, as well as the driver's list of active orders, periodically poll the database with a timer (`QTimer`) and refresh the data on the screen.

### Order Lifecycle

An order goes through the states `Поиск` ("searching") → `Выполнение` ("in progress") → `Завершен` ("completed"), or `Отменен` ("cancelled") at the client's initiative.

## Interface

The interface (in Russian) is split by role: after login, the menu of the corresponding role opens. The window layouts were created in Qt Designer (`ui maket/`).

| Role | Main sections |
| ---- | ------------- |
| Client | Order a taxi, Chat, Feedback, Order history, Help |
| Driver | Active orders, Chat, About the car, Order history, Feedback, Help |
| Administrator | Orders, Clients, Employees, Cars, Feedback, Support chats |

<table>
  <tr>
    <td align="center"><img src="image/gui_login.png" width="400"><br><sub>Login</sub></td>
    <td align="center"><img src="image/gui_client_order.png" width="400"><br><sub>Client: ordering a taxi</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="image/gui_driver_orders.png" width="400"><br><sub>Driver: active orders</sub></td>
    <td align="center"><img src="image/gui_driver_accepted.png" width="400"><br><sub>Driver: accepted order</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="image/gui_chat.png" width="400"><br><sub>Driver–client chat</sub></td>
    <td align="center"><img src="image/gui_feedback.png" width="400"><br><sub>Feedback and rating after the ride</sub></td>
  </tr>
</table>

## Application Architecture

The entry point is `main.py`: the login window (`MainWindow`) and the registration window (`RegisterWindow`). After login, the window of the role opens:

- `cl_int.py` — client (`ZakCl` and related windows: order, waiting, chat, feedback, history);
- `vod_int.py` — driver (`Vodila`: active orders, accepted order, chat, car maintenance, history);
- `adm_int.py` — administrator (`Admin`: orders, clients, employees, cars, feedback, support chats).

The windows are built on classes generated from Qt Designer layouts (`interface/`) and share common resources (`image/`). UML class diagram:

![UML class diagram](image/uml_classes.png)

## Technologies Used

| Technology | Purpose |
| ---------- | ------- |
| [Python 3](https://www.python.org/) | Language of the client application |
| [MySQL](https://www.mysql.com/) 8 | DBMS: tables, keys, procedures, triggers |
| [MySQL Workbench](https://www.mysql.com/products/workbench/) | Schema modeling and SQL script development |
| [PyQt6](https://pypi.org/project/PyQt6/) | Graphical interface (`QtWidgets`, `QtCore`, `QtGui`), `QTimer` timers |
| Qt Designer | Window layouts (`.ui`) |
| [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/) | Connecting to MySQL, calling procedures (`callproc`) and running queries |
| `random`, `datetime`, `sys` | Standard library |
| PyCharm Community | Development environment |

## Installation and Usage

1. Install [Python 3](https://www.python.org/downloads/) and [MySQL Server 8](https://dev.mysql.com/downloads/mysql/).
2. Install the dependencies:

   ```bash
   pip install PyQt6 mysql-connector-python
   ```

3. Create the `taxi` database and import a dump into it: tables, stored procedures, triggers and the `audit_log` table.

4. Set your own connection parameters in `config.py`:

   ```python
   host = "localhost"
   user = "your_user"
   password = "your_password"
   db_name = "taxi"
   ```

5. Run the application from the project's root folder:

   ```bash
   git clone https://github.com/DenkiGO/Taxi_app.git
   cd Taxi_app
   python main.py
   ```

For the interface to render correctly, installing the **Istok Web** font is recommended.