# PostgreSQL Setup Guide for Manjaro

This guide will help you install PostgreSQL on Manjaro and connect it to your Django project.

## Step 1: Install PostgreSQL

Run the following command in your terminal:

```bash
sudo pacman -S postgresql
```

## Step 2: Initialize PostgreSQL Database Cluster

After installation, you need to initialize the database cluster:

```bash
sudo -u postgres initdb -D /var/lib/postgres/data
```

## Step 3: Start PostgreSQL Service

Enable and start the PostgreSQL service:

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

To check if PostgreSQL is running:

```bash
sudo systemctl status postgresql
```

## Step 4: Create Database and User

Switch to the postgres user and create a database and user for your Django project:

```bash
sudo -u postgres psql
```

Once in the PostgreSQL prompt, run these commands:

```sql
-- Create a new user
CREATE USER mend_user WITH PASSWORD 'mend_password';

-- Create the database
CREATE DATABASE mend_db OWNER mend_user;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE mend_db TO mend_user;

-- Exit PostgreSQL
\q
```

**Important:** Change `'mend_password'` to a secure password of your choice, and update it in `mend/settings.py` as well.

## Step 5: Update Django Settings

The Django settings have already been updated to use PostgreSQL. If you changed the password in Step 4, make sure to update it in:

`mend/mend/settings.py`

The current database configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mend_db',
        'USER': 'mend_user',
        'PASSWORD': 'mend_password',  # Update this if you changed it
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Step 6: Run Migrations

After setting up PostgreSQL, run Django migrations to create the database tables:

```bash
cd /home/whoami/Documents/Builds/Mend/mend_backend/mend
source ../venv/bin/activate
python manage.py migrate
```

## Step 7: Create a Superuser (Optional)

If you want to access the Django admin panel:

```bash
python manage.py createsuperuser
```

## Troubleshooting

### PostgreSQL service won't start
- Check if the data directory exists: `ls -la /var/lib/postgres/data`
- Check logs: `sudo journalctl -u postgresql`

### Connection refused error
- Make sure PostgreSQL is running: `sudo systemctl status postgresql`
- Check if PostgreSQL is listening on port 5432: `sudo ss -tlnp | grep 5432`

### Authentication failed
- Verify the password in `settings.py` matches the one you set in PostgreSQL
- Check PostgreSQL authentication settings in `/var/lib/postgres/data/pg_hba.conf`

### Permission denied
- Make sure the `mend_user` has proper permissions on the database
- You can verify with: `sudo -u postgres psql -c "\du"` (lists all users)

## Useful PostgreSQL Commands

```bash
# Connect to PostgreSQL as postgres user
sudo -u postgres psql

# Connect to your database
sudo -u postgres psql -d mend_db

# List all databases
sudo -u postgres psql -c "\l"

# List all users
sudo -u postgres psql -c "\du"

# Drop database (if needed)
sudo -u postgres psql -c "DROP DATABASE mend_db;"

# Drop user (if needed)
sudo -u postgres psql -c "DROP USER mend_user;"
```

