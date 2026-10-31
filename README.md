# Raffle Dashboard

A Flask web dashboard for sneaker raffle entry automation, task management, proxy pools, and Discord webhook notifications.

## Features

- **Dashboard Overview**: Monitor active raffles, submitted entries, and account/balance status.
- **Task Management**: Configure automated entry tasks with sneaker sizes, entry limits, and linked profiles/proxies.
- **Proxy Pool Manager**: Bulk import proxies, organize proxy groups, and filter valid host:port lists.
- **Profiles & Billing**: Manage shipping addresses and billing profiles.
- **Webhook Notifications**: Real-time Discord embeds for task status and raffle submission updates.
- **User Roles & Administration**: Role-based permissions (Admin / User), user invitations, and account settings.
- **Anti-Captcha Integration**: Integrated balance check and solver key management.

## Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, RQ, WTForms
- **Database**: PostgreSQL / SQLite
- **Cache & Queue**: Redis
- **Frontend**: Jinja2 templates, Bootstrap 4, SCSS

## Getting Started

### 1. Prerequisites
- Python 3.8+
- PostgreSQL
- Redis

### 2. Environment Setup
Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 3. Configuration
Create a `config.env` file in the project root:

```env
SECRET_KEY=your_generated_secret_key
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin123
WEBHOOK_TEST_URL=https://discord.com/api/webhooks/your_webhook_url
```

### 4. Database Setup
Initialize the schema and seed default roles:

```bash
python manage.py recreate_db
python manage.py setup_dev

# Optional: populate fake data for testing
python manage.py add_fake_data
```

### 5. Run
```bash
honcho start -e config.env -f Local
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.
