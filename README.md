# Music Library Web App

This is a Django-based web application for managing a music library.

## Features

- Add new music with title, artist, album, year, genre, image, and audio file
- View and edit existing music entries
- Delete music entries
- Search and filter music entries by various criteria
- User authentication and authorization
- Responsive design for desktop browsers

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/pedramkarimii/music-library.git
    ```

2. Navigate into the project directory:

    ```
    cd music-library
    ```

3. Create a virtual environment:

    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

5. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Run migrations to create the database:

    ```
    python manage.py migrate
    ```

7. Create a superuser account (admin):

    ```
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```
    python manage.py runserver
    ```

9. Access the web application at http://localhost:8000/ in your web browser.

## Usage

- Log in using your admin account to access the admin interface at `/admin/`.
- Use the admin interface to add, edit, or delete music entries.
- Navigate to the main application interface to view and search music entries.
- Use the "Add Music" link to add new music entries to the library.


