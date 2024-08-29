Dice Game Project
This is a simple web-based Dice Game developed using Flask, a lightweight web framework for Python. The game allows two players to compete against each other, with the goal of reaching a score of 20 or more first.

Features
Two-player Game: Players take turns rolling a dice to accumulate points.
Interactive Interface: Players can choose to either roll the dice or hold their current score.
Dynamic Dice Images: The result of the dice roll is displayed as an image.
Sound Effects: Sound effects are included for rolling the dice and when a player wins.
Winner Declaration: The game declares a winner when a player's score reaches or exceeds 20 points.
Reset Option: Players can restart the game and enter their names again.
Installation
To get the Dice Game up and running on your local machine or server, follow these steps:

Prerequisites
Python 3.x
pip (Python package installer)
Git (if cloning from GitHub)
An Ubuntu server (if deploying on AWS EC2)
Clone the Repository
Clone this repository to your local machine or server using Git:

bash
Kodu kopyala
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Install Dependencies
Install the necessary Python packages using pip:

bash
Kodu kopyala
pip3 install -r requirements.txt
Running the Application
To run the Flask application locally:


flask run --host=0.0.0.0
This will start the server on http://0.0.0.0:5000.

Deployment on AWS EC2
If you want to deploy the application on an AWS EC2 instance:

SSH into your EC2 instance.
Clone the repository or upload the project files.
Install Python dependencies as described above.
Run the Flask application:

flask run --host=0.0.0.0
Ensure the appropriate port is open in your EC2 instance's security group (e.g., port 5000).
Accessing the Application
Locally: Visit http://127.0.0.1:5000 in your browser.
On EC2: Visit http://your-ec2-public-ip:5000 in your browser.
Project Structure
app.py: The main Flask application file that handles routing and game logic.
templates/: Directory containing HTML templates.
index.html: The initial page where players enter their names.
game.html: The main game interface.
winner.html: The page displayed when a player wins.
static/: Directory containing static files (CSS, JavaScript, images, sounds).
styles.css: Custom styles for the application.
script.js: JavaScript for dice animations and sound effects.
dice_images/: Directory containing dice image files.
sounds/: Directory containing sound effect files.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Issues and suggestions are also welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Flask community for providing a robust framework.
Sound effects sourced from [https://pixabay.com/].
