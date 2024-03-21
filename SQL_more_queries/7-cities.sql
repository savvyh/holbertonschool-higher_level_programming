-- Create a new table inside the last database created.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256),
    state_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
