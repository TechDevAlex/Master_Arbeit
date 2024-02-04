-- Create a users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id serial PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (100) NOT NULL
);

-- Insert sample data with ON CONFLICT DO NOTHING
INSERT INTO users (username, password)
VALUES
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3')
ON CONFLICT (username) DO NOTHING;
