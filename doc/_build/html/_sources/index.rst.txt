.. OC lettings site documentation master file, created by
   sphinx-quickstart on Mon Sep  2 15:47:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. OC lettings site documentation master file, created by
   sphinx-quickstart on Mon Sep  2 15:47:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


OC Lettings Site Documentation
==============================

Technical Specifications
=========================

Overview
--------

Orange County Lettings is a rapidly expanding startup in the real estate rental sector, aiming to establish a strong presence in the United States.

The project involves developing and enhancing the company's website, focusing on code improvements, deployment strategies, and resolving existing issues.

As part of the team, you are responsible for improving the website's functionality, optimizing the codebase, and ensuring smooth deployment processes.

Key Responsibilities
~~~~~~~~~~~~~~~~~~~~~

- Execute the site locally, navigate it, and ensure functionality.
- Access and manage the admin section.
- Interact with the database, running queries and managing data.
- Run linting and test suites locally.

Installation Instructions
==========================

Prerequisites
-------------

- GitHub account with read access to the repository.
- Git CLI.
- SQLite3 CLI.
- Python interpreter (version 3.7 or higher).
- Docker.

Setup Steps
-----------

1. **Clone the Repository**:
   - Navigate to the desired directory: ``cd /path/to/put/project/in``
   - Clone the repository: ``git clone https://github.com/br-imen/Python-OC-Lettings-FR.git``

2. **Create and Activate Virtual Environment**:
   - Navigate to the project directory: ``cd /path/to/Python-OC-Lettings-FR``
   - Create a virtual environment: ``python -m venv venv``
   - Activate the environment: ``source venv/bin/activate``
   - Verify Python interpreter: ``which python``
   - Confirm Python version: ``python --version``

3. **Install Dependencies**:
   - Install required Python packages: ``pip install -r requirements.txt``

4. **Database Setup**:
   - Apply migrations: ``python manage.py migrate``

5. **Run the Server**:
   - Start the development server: ``python manage.py runserver``

Quick Start Guide
=================

Running the Project
-------------------

- Start the local server using ``python manage.py runserver``.
- Access the website at ``http://127.0.0.1:8000/``.

Accessing the Admin Interface
-----------------------------

- Navigate to ``http://127.0.0.1:8000/admin/`` to access the admin section.
- Use provided credentials to log in and manage data.

Running Tests
-------------

- Execute the test suite using Pytest: ``pytest``
- Generate a coverage report: ``coverage run -m pytest && coverage report``

Technologies and Programming Languages
======================================

- **Backend**: Django (Python)
- **Database**: SQLite3
- **Containerization**: Docker
- **Error Monitoring**: Sentry
- **Testing**: Pytest, Coverage
- **CI/CD Pipeline**: GitHub Actions
- **Hosting**: Render 

Database Structure and Data Models
==================================

Database Overview
-----------------

The database is managed by Django's ORM and uses SQLite3.

The original monolithic architecture has been modularized into separate apps: ``lettings`` and ``profiles``.

Models
------

Detailed Model Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Address
~~~~~~~

The `Address` model represents a physical address, including the number, street, city, state, zip code, and country ISO code.

- **Fields**:
  - `number`: A positive integer field representing the street number. It has a maximum value of 9999.
  - `street`: A character field for the street name with a maximum length of 64 characters.
  - `city`: A character field for the city name with a maximum length of 64 characters.
  - `state`: A character field representing the state, restricted to exactly 2 characters (e.g., "CA" for California).
  - `zip_code`: A positive integer field for the zip code, with a maximum value of 99999.
  - `country_iso_code`: A character field for the country ISO code, restricted to exactly 3 characters (e.g., "USA").

- **Meta Options**:
  - `verbose_name_plural`: Set to "Addresses" to correct the pluralization of the model name in the Django admin.

- **Methods**:
  - `__str__(self)`: Returns a string representation of the address, consisting of the street number and street name (e.g., "123 Main St").

Letting
~~~~~~~

The `Letting` model represents a property available for rent. It includes a title and is linked to an `Address` instance.

- **Fields**:
  - `title`: A character field for the title of the letting, with a maximum length of 256 characters.
  - `address`: A one-to-one relationship to the `Address` model, indicating that each letting is associated with a single address.

- **Methods**:
  - `__str__(self)`: Returns the title of the letting.

Profile
~~~~~~~

The `Profile` model represents a user's profile within the application. It is linked to Django's built-in `User` model using a one-to-one relationship. Each profile stores the user's favorite city.

- **Fields**:
  - `user`: A one-to-one relationship to the `User` model. This ensures that each user has one unique profile.
  - `favorite_city`: A character field that stores the user's favorite city, with a maximum length of 64 characters. This field is optional, as indicated by `blank=True`.

- **Methods**:
  - `__str__(self)`: Returns the username associated with the profile, which makes it easier to identify profiles in the Django admin interface and other parts of the application.

Migrations
----------

Data migration from the old structure to the new modular structure was handled using Django migrations without direct SQL.


Profiles App - Interface Description
====================================

URLs (URLconf)
--------------

- **Profiles Index Page**:
  - **URL**: `/profiles/`
  - **View**: `index`
  - **Name**: `profiles_index`
  - **Description**: This URL maps to the profiles index view, which displays a list of all user profiles.
  - **Parameters**: None

- **User Profile Page**:
  - **URL**: `/profiles/<str:username>/`
  - **View**: `profile`
  - **Name**: `profile`
  - **Description**: This URL maps to the profile view, which displays detailed information about a specific user profile.
  - **Parameters**: 
    - `username` (str): The username of the profile to be displayed.

Views
-----

- **Index View** (`index`)
  - **Description**: Renders a list of all user profiles.
  - **Template**: `profiles/index.html`
  - **Context**:
    - `profiles_list`: A queryset of all `Profile` objects in the database.
  - **Accessed by**: `/profiles/`

- **Profile View** (`profile`)
  - **Description**: Renders detailed information about a specific user profile.
  - **Template**: `profiles/profile.html`
  - **Context**:
    - `profile`: The `Profile` object associated with the specified username.
  - **Accessed by**: `/profiles/<str:username>/`

Templates
---------

- **profiles/index.html**
  - **Description**: Displays a list of all profiles with links to individual profile pages.
  - **Context Variables**:
    - `profiles_list`: List of all `Profile` objects.
  - **URL References**:
    - Link to individual profile pages using `{% url 'profiles:profile' username=profile.user.username %}`.
    - Navigation links to Home and Lettings pages.

- **profiles/profile.html**
  - **Description**: Displays detailed information about a specific user, including their first name, last name, email, and favorite city.
  - **Context Variables**:
    - `profile`: The `Profile` object to be displayed.
  - **URL References**:
    - Navigation links to Profiles Index, Home, and Lettings pages.


Lettings App - Interface Description
====================================

URLs (URLconf)
--------------

- **Lettings Index Page**:
  - **URL**: `/lettings/`
  - **View**: `index`
  - **Name**: `lettings_index`
  - **Description**: This URL maps to the lettings index view, which displays a list of all available lettings.
  - **Parameters**: None

- **Letting Detail Page**:
  - **URL**: `/lettings/<int:letting_id>/`
  - **View**: `letting`
  - **Name**: `letting`
  - **Description**: This URL maps to the letting detail view, which displays detailed information about a specific letting.
  - **Parameters**: 
    - `letting_id` (int): The ID of the letting to be displayed.

Views
-----

- **Index View** (`index`)
  - **Description**: Renders a list of all lettings available in the system.
  - **Template**: `lettings/index.html`
  - **Context**:
    - `lettings_list`: A queryset of all `Letting` objects in the database.
  - **Accessed by**: `/lettings/`

- **Letting View** (`letting`)
  - **Description**: Renders detailed information about a specific letting.
  - **Template**: `lettings/letting.html`
  - **Context**:
    - `title`: The title of the letting.
    - `address`: The `Address` object associated with the letting.
  - **Accessed by**: `/lettings/<int:letting_id>/`

Templates
---------

- **lettings/index.html**
  - **Description**: Displays a list of all lettings with links to individual letting detail pages.
  - **Context Variables**:
    - `lettings_list`: List of all `Letting` objects.
  - **URL References**:
    - Link to individual letting detail pages using `{% url 'lettings:letting' letting_id=letting.id %}`.
    - Navigation links to Home and Profiles pages.

- **lettings/letting.html**
  - **Description**: Displays detailed information about a specific letting, including the address.
  - **Context Variables**:
    - `title`: The title of the letting.
    - `address`: The `Address` object related to the letting.
  - **URL References**:
    - Navigation links to Lettings Index, Home, and Profiles pages.


User Guide with Common Use Cases
================================

Profiles App
------------

Overview
~~~~~~~~

The `profiles` app allows users to view and manage profiles within the system. Each profile is associated with a Django `User` model and contains additional information such as the user's favorite city.

Common Use Cases
~~~~~~~~~~~~~~~~

1. **Viewing All Profiles**
   - **Objective**: To browse a list of all user profiles in the system.
   - **Steps**:
     1. Navigate to the URL `/profiles/`.
     2. The system will display a list of all profiles, with each username linking to the corresponding profile detail page.
     3. Click on any username to view detailed information about that specific user profile.

2. **Viewing a Specific User Profile**
   - **Objective**: To view detailed information about a specific user.
   - **Steps**:
     1. Navigate to the URL `/profiles/<username>/`, replacing `<username>` with the actual username of the user whose profile you wish to view.
     2. The system will display detailed information about the user, including their first name, last name, email address, and favorite city.
     3. You can navigate back to the list of profiles or to the home page using the provided navigation buttons.

3. **Navigating Between Sections**
   - **Objective**: To easily navigate between the profiles section, home page, and lettings section.
   - **Steps**:
     1. On any profile-related page (list or detail), use the navigation buttons at the bottom of the page.
     2. These buttons will direct you to the Home page, the Profiles list, or the Lettings section.


Lettings App
------------

Overview
~~~~~~~~

The `lettings` app allows users to view and manage rental properties (lettings) within the system. Each letting is associated with an `Address` and includes details about the rental property.

Common Use Cases
~~~~~~~~~~~~~~~~

1. **Viewing All Lettings**
   - **Objective**: To browse a list of all rental properties available in the system.
   - **Steps**:
     1. Navigate to the URL `/lettings/`.
     2. The system will display a list of all lettings, with each title linking to the corresponding letting detail page.
     3. Click on any title to view detailed information about that specific rental property.

2. **Viewing a Specific Letting**
   - **Objective**: To view detailed information about a specific rental property.
   - **Steps**:
     1. Navigate to the URL `/lettings/<letting_id>/`, replacing `<letting_id>` with the actual ID of the letting you wish to view.
     2. The system will display detailed information about the rental property, including the address (street number, street name, city, state, zip code, and country ISO code).
     3. You can navigate back to the list of lettings or to the home page using the provided navigation buttons.

3. **Navigating Between Sections**
   - **Objective**: To easily navigate between the lettings section, home page, and profiles section.
   - **Steps**:
     1. On any letting-related page (list or detail), use the navigation buttons at the bottom of the page.
     2. These buttons will direct you to the Home page, the Lettings list, or the Profiles section.


Deployment and Application Management Procedures
================================================

Deployment
----------

The project is deployed using a CI/CD pipeline configured in GitHub Actions. This pipeline automates the process of testing, building, and deploying the application to ensure consistent and reliable deployments.

Steps
-----

1. **Set Up a New Application in Render**:
   
   - **Create a New Web Service**:
     - Log in to your Render account and create a new web service.
     - Select "Docker" as the environment type.
     - Provide the Docker image URL from Docker Hub where your application image will be stored.
     - Save the initial setup.

   - **Configure Render Secrets**:
     - Add the following secrets as "Secret Files" in the Render dashboard:
       - **``SENTRY_DSN``**: The Data Source Name for Sentry, used for logging and error monitoring.
       - **``SECRET_KEY``**: The Django secret key used for cryptographic operations.
       - **``ALLOWED_HOSTS``**: A comma-separated list of allowed hosts for the Django application.
     
   - **Set Render Environment Variables**:
     - Add the following environment variables:
       - **``DEBUG``**: Set to `False` for production environments.
       - **``ENVIRONMENT``**: Set to the appropriate environment name, e.g., `production` or `staging`.
     
   - **Retrieve the Deploy Hook URL and Hostname**:
     - After configuring the secrets and environment variables, save the settings.
     - Retrieve the deployment webhook URL from Render, which will be used to trigger deployments.
     - Note down the hostname provided by Render, as it will be used in the `ALLOWED_HOSTS` setting.

2. **Configure GitHub Secrets**:
   
   - Access your GitHub repository settings and navigate to "Secrets and variables > Actions secrets".
   - Add the following secrets:
     - **``SECRET_KEY``**: This is a crucial security component used by Django for cryptographic operations, such as signing cookies or hashing passwords. Ensure this value is strong and unique.
     - **``DOCKER_HUB_USERNAME`` and ``DOCKER_HUB_PASSWORD``**: These are the credentials used to authenticate with Docker Hub. They allow the CI/CD pipeline to push the built Docker images to your Docker Hub repository.
     - **``RENDER_DEPLOY_HOOK_URL``**: This is the webhook URL provided by Render that triggers the deployment process automatically whenever new changes are pushed to the repository.

3. **Docker Hub**: A Docker Hub account is required to store the Docker image of the application. Docker Hub acts as a registry where the CI/CD pipeline pushes the image, making it accessible for deployment.

   **Setting Up Docker Hub**:

   - Create an account on Docker Hub if you haven't already.
   - Create a new repository on Docker Hub to store your application's Docker images.
   - Make sure your repository is set to "private" if you don't want the image to be publicly accessible.

4. **Service d'Hébergement (Render)**: The application is deployed on Render, which supports containerized deployments via Docker images. Render pulls the Docker image from Docker Hub and deploys it automatically whenever the webhook is triggered.

   **Configuring Render**:

   - Log in to your Render account.
   - Create a new web service, select "Docker" as the environment type, and provide the Docker image URL from Docker Hub.
   - Configure the necessary secrets (`SENTRY_DSN`, `SECRET_KEY`, `ALLOWED_HOSTS`) and environment variables (`DEBUG`, `ENVIRONMENT`) in Render.
   - Retrieve the deployment webhook URL and hostname from Render.

Deployment Steps
----------------

1. **Trigger the Deployment**:
   
   - Push your changes to the ``master`` branch or merge a pull request into ``master``.
   - The CI/CD pipeline will automatically execute:
     - Tests will be run first to verify the integrity of the code.
     - Next, a Docker image will be built and pushed to Docker Hub.
     - Finally, the application will be deployed on Render using the deployment webhook.

2. **Verify the Deployment**:
   
   - Access your application’s URL on Render to ensure that the deployment was successful and that the application is functioning as expected.

By following these instructions, your successor will be able to deploy the application reliably and efficiently, ensuring continuity in the delivery process.

Monitoring
----------

- Logs and error monitoring are managed through Sentry.
- Regular backups of the SQLite3 database are recommended.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

