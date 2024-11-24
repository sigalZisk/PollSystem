DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS answers;

CREATE TABLE questions (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL
);

CREATE TABLE options (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question_id INT(11) NOT NULL,
    text VARCHAR(300) NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE answers (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    user_id INT(11) NOT NULL,
    question_id INT(11) NOT NULL,
    option_id INT(11) NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id),
    FOREIGN KEY (option_id) REFERENCES options(id)
);

INSERT INTO questions (title) VALUES
    ("What type of cuisine are you in the mood for?"),
    ("What is your preferred price range for the meal?"),
    ("How many people will be dining with you?"),
    ("Do you have any dietary restrictions or preferences?"),
    ("What's the occasion?"),
    ("What atmosphere are you looking for?"),
    ("How important is the location and convenience of the restaurant to you?"),
    ("Do you have any must-have features?"),
    ("Are you looking for a new-to-you place, or a restaurant you'd visited before?"),
    ("How important are online reviews in your restaurant selection process?");


INSERT INTO options (question_id, text) VALUES
    (1, "Italian"),
    (1, "Mexican"),
    (1, "Chinese"),
    (1, "Other"),
    (2, "50 - 100 per person"),
    (2, "100 - 200 per person"),
    (2, "200 - 300 per person"),
    (2, "More than 300 per person"),
    (3, "Just me"),
    (3, "Me and a friend"),
    (3, "A small group (3 - 10)"),
    (3, "More than 10"),
    (4, "Not at all"),
    (4, "Vegetarian"),
    (4, "Gluten-free"),
    (4, "Vegan"),
    (5, "No special occasion"),
    (5, "A birthday celebration"),
    (5, "A wedding proposal"),
    (5, "A date"),
    (6, "Quiet and intimate"),
    (6, "Lively and energetic"),
    (6, "Family-friendly"),
    (6, "Pet-friendly"),
    (7, "Not so much"),
    (7, "It needs to be nearby"),
    (7, "It needs to be convenient"),
    (7, "It needs to have a parking lot"),
    (8, "Outdoor seating"),
    (8, "Views"),
    (8, "Live music"),
    (8, "Other"),
    (9, "A new-to-me"),
    (9, "One I've visited a lot"),
    (9, "One I've visited a little"),
    (9, "I Don't mind"),
    (10, "Very much"),
    (10, "Not so much"),
    (10, "Very little"),
    (10, "Not at all");
