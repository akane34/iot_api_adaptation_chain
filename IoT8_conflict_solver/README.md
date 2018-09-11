# IoT8 Conflict Solver
Solves comparison differentials.

## Start up

### Install dependencies
pip install -r requirements.txt

### Set environment variables
SQLALCHEMY_DATABASE_URI = ''

### Start database
flask db init
flask db migrate
flask db upgrade

### Start server
python main.py runserver
