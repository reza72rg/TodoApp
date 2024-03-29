# Todo List Program

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This is a Todo List program built with Django, which allows users to record and manage their daily tasks. The program provides a user-friendly interface to prevent forgetting important tasks. It also includes a REST API to retrieve data from the program. The project is Dockerized for easy deployment and management.

## Features

- **Todo List Management**: Users can create, update, and delete tasks in their todo list.
- **User Authentication**: The program uses the Django `AbstractBaseUser` to customize the user model, providing secure user authentication.
- **Docker Support**: The project includes a Docker structure for easy deployment and management.
- **API Support**: The app includes a REST API that allows users to interact with the app's functionality programmatically. The API documentation can be found at `http://127.0.0.1:8000/swagger/`.
- **Email Verification**: The app uses the `smtp4dev` element in the Docker file format to send emails and verify user accounts.
- **Testing**: The app includes unit tests written with `pytest` to ensure the correctness of different parts of the app.
- **Random Data Generation**: The app utilizes the `faker` library to create random data for testing and populating the database.
- **Performance Testing**: The app includes an API tolerance threshold that allows testing the performance using artificial traffic generated by Locust. The performance testing can be accessed at `http://127.0.0.1:8089/`.
- **Background Tasks**: The app explores the use of background tasks in Django projects by integrating with Brokers like Redis and using the Celery module to create and manage different tasks.
- **Caching**: The app implements caching of information in different views using Redis to improve performance.

## Installation

1. Clone this repository to your local machine:

   
bash
   git clone https://github.com/reza72rg/TodoApp
   
2. Install the required dependencies:

   
bash
   pip install -r requirements.txt
   
3. Set up the database by running migrations:

   
bash
   python manage.py migrate
   
4. Start the development server:

   
bash
   python manage.py runserver
   
5. Open the program in your web browser at `http://127.0.0.1:8000`.

## API Documentation

The API documentation can be found at `http://127.0.0.1:8000/api/v1/` and `http://127.0.0.1:8000/accounts/api/v1/`, providing details on how to interact with the REST API endpoints.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Special thanks to [Ali Bigdali] for their assistance and feedback during the development of this project.

## Performance Testing

Using Locust, the API tolerance threshold is created and its performance is checked by generating artificial traffic on the site. It can be tested at the address `http://127.0.0.1:8089/`.