# TODO API

## Details

### Key Features:

 - Django Rest Framework: Implemented RESTful endpoints to facilitate seamless communication between the front and back end, ensuring optimal performance and scalability.
 - PostgreSQL Database: Designed and maintained a PostgreSQL database to store and manage TODO tasks efficiently, ensuring data integrity and reliability.
 - User Authentication: Implemented secure authentication mechanisms using Tokens to control access to the TODO API, prioritizing data security and privacy.

<div align="center">
   <img src="./assets/images/cover.png">
</div>

## ⚙ Tools and Technologies used

1. [Python](https://www.python.org/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)
3. [PostgreSQL](https://www.postgresql.org/)

## 🛠 Installation and setup

1. Install Docker [here](https://www.docker.com/get-started/)
2. Install Git [here](https://git-scm.com/downloads)
3. Create a working directory:

   ```bash
   mkdir ~/TODO && cd ~/TODO
   ```

4. Clone the repository

   ```bash
   git clone https://github.com/ak4m410x01/TODO_API/ .
   ```

5. Start the application

   ```bash
    docker-compose up -d
   ```

6. Access API: http://127.0.0.1:8000/api/

7. Access DB: 127.0.0.1:5432

8. Don't forget .env file with variables

| Variable          | Value                                                                 |
| ----------------- | --------------------------------------------------------------------- |
| SECRET_KEY        | "django-insecure-%2dmqnqj9v2e&8yk\*t=#b+2-=i!45+153*@-g0*=&%1od16z^m" |
| DEBUG             | False                                                                 |
| DATABASE_ENGINE   | "django.db.backends.postgresql"                                       |
| DATABASE_HOST     | "db"                                                                  |
| DATABASE_PORT     | "5432"                                                                |
| DATABASE_NAME     | "todo"                                                                |
| DATABASE_USER     | "todo"                                                                |
| DATABASE_PASSWORD | "todo"                                                                |
| POSTGRES_DB       | "todo"                                                                |
| POSTGRES_USER     | "todo"                                                                |
| POSTGRES_PASSWORD | "todo"                                                                |

you can use this .env file [here](./.env)

note:
these variables are for the lab environment only... don't use these in xxx production environments xxx

---

## Todo Database Schema

#### 1. users

    +------------+---------+----------------------+
    | Field      | Type    | Use                  |
    | ---------- | ------- | -------------------- |
    | id         | INTEGER | To Store primary key |
    | username   | VARCHAR | To store username    |
    | password   | VARCHAR | To store password    |
    | first_name | VARCHAR | To store first name  |
    | last_name  | VARCHAR | To store last name   |
    | email      | VARCHAR | To store email       |
    +------------+---------+----------------------+

<br />

#### 2. tasks

    +-------------+-------------+-----------------------+
    | Field       | Type        | Use                   |
    | ----------- | ----------- | --------------------- |
    | id          | INTEGER     | To Store primary key  |
    | title       | VARCHAR     | To Store title        |
    | description | VARCHAR     | To Store description  |
    | start_time  | TIMESTAMP   | to store start time   |
    | end_time    | TIMESTAMP   | to store end time     |
    | done        | BOOL        | to store state        |
    | created_at  | TIMESTAMP   | to store created time |
    | updated_at  | TIMESTAMP   | to store created time |
    | user        | Foreign key | to store user         |
    +-------------+-------------+-----------------------+

---

## API Endpoints

- base_url: http://127.0.0.1:8000/api/

  - Users:

        +--------------------------------------------+---------------------+
        | Endpoints                                  | Use                 |
        | ------------------------------------------ | ------------------- |
        | POST `{{base_url}}/api/users/`             | Rgister New User    |
        | GET `{{base_url}}/api/tasks/<int:id>/`     | Get User Details    |
        | PUT `{{base_url}}/api/tasks/<int:id>/`     | Update User Details |
        | DELETE `{{base_url}}/api/tasks/<int:id>/`  | Delete Task         |
        +--------------------------------------------+---------------------+

  - Tasks

        +--------------------------------------------+---------------------+
        | Endpoints                                  | Use                 |
        | ------------------------------------------ | ------------------- |
        | GET `{{base_url}}/api/tasks/`              | List All Tasks      |
        | POST `{{base_url}}/api/tasks/`             | Create New Task     |
        | GET `{{base_url}}/api/tasks/<int:id>/`     | Get Task Details    |
        | PUT `{{base_url}}/api/tasks/<int:id>/`     | Update Task Details |
        | DELETE `{{base_url}}/api/tasks/<int:id>/`  | Delete Task         |
        +--------------------------------------------+---------------------+

  - Token

        +--------------------------------------------+----------------------+
        | Endpoints                                  | Use                  |
        | ------------------------------------------ | -------------------- |
        | GET `{{base_url}}/token/`                  | Get Token            |
        | POST `{{base_url}}/token/`                 | Regenerate New Token |
        +--------------------------------------------+----------------------+

---

## PIP Packages

    +---------------------+---------+-------------------+
    | Name                | Version | Use               |
    | ------------------- | ------- | ----------------- |
    | Python              | 3.11.6  | Programming Lang  |
    | djangorestframework | 3.14.0  | Restful framework |
    | psycopg2-binary     | 2.9.9   | PostgreSQL DB lib |
    | python-dotenv       | 1.0.0   | To use .env file  |
    +---------------------+---------+-------------------+
