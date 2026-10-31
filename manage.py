#!/usr/bin/env python
import argparse
import os

from flask_migrate import Migrate
from app import create_app, db
from app.models import Role, User, Product, Task
from config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


def recreate_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
        print("Database recreated successfully.")


def setup_dev():
    with app.app_context():
        Role.insert_roles()
        admin_query = Role.query.filter_by(name='Administrator')
        if admin_query.first() is not None:
            if User.query.filter_by(email=Config.ADMIN_EMAIL).first() is None:
                user = User(
                    username='admin',
                    password=Config.ADMIN_PASSWORD,
                    confirmed=True,
                    email=Config.ADMIN_EMAIL)
                db.session.add(user)
                db.session.commit()
                print(f"Added administrator ({Config.ADMIN_EMAIL})")


def add_fake_data(count=10):
    with app.app_context():
        User.generate_fake(count=count)
        Product.generate_fake(count=count)
        Task.generate_fake(count=count)
        print(f"Added fake data for {count} records.")


def run():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Manage Raffle Dashboard")
    parser.add_argument('command', choices=['run', 'recreate_db', 'setup_dev', 'add_fake_data'])
    parser.add_argument('-n', '--number-users', type=int, default=10)
    args = parser.parse_args()

    if args.command == 'run':
        run()
    elif args.command == 'recreate_db':
        recreate_db()
    elif args.command == 'setup_dev':
        setup_dev()
    elif args.command == 'add_fake_data':
        add_fake_data(args.number_users)
