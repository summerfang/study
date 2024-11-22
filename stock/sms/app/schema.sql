-- database/schema.sql

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('Admin', 'Operator')),
    merchant_id INTEGER REFERENCES merchants(id) NOT NULL
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    user_id INTEGER REFERENCES users(id) NOT NULL
);

CREATE TABLE phone_numbers (
    id SERIAL PRIMARY KEY,
    merchant_id INTEGER REFERENCES merchants(id) NOT NULL,
    number VARCHAR(20) UNIQUE NOT NULL,
    customer_id INTEGER REFERENCES customers(id)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE project_phone_numbers (
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    phone_number_id INTEGER REFERENCES phone_numbers(id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, phone_number_id)
);

CREATE TABLE sms_messages (
    id SERIAL PRIMARY KEY,
    from_number_id INTEGER REFERENCES phone_numbers(id) NOT NULL,
    to_number_id INTEGER REFERENCES phone_numbers(id) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc') NOT NULL,
    status VARCHAR(50) NOT NULL
);