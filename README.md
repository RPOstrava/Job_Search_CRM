# Job Search CRM

A lightweight application tracking system built with Python and Flask to help me better organize my work requests.

## Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML, CSS (Clean Tech Design)

## Features
* Add, edit, and delete job applications (Full CRUD).
* Filter applications by status.
* Automatic sorting from the newest applications (`sent_date DESC`).
* Automatic database initialization on startup.

## Local Data & Localization
The application stores the following information for each job application:

| Czech              | English   |
| ------------------ | --------- |
| **Firma**          | Company   |
| **Pozice**         | Position  |
| **Stav**           | Status    |
| **Datum odeslání** | Date Sent |

The user interface and sample data are intentionally in Czech because the application was developed for tracking job applications in the Czech job market. This provides a realistic example of the application's intended use while keeping the project suitable for demonstration purposes.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone 