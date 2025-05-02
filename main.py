from flask import Flask, render_template_string, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        token = request.form.get("token")
        message = request.form.get("message")
        # Facebook login or any action using Selenium
        if token:
            try:
                # Set up the driver (use Chrome or any other driver you want)
                driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
                driver.get('https://www.facebook.com')

                # Log in with token
                driver.add_cookie({'name': 'c_user', 'value': token})
                driver.get('https://www.facebook.com/messages')

                # Wait for the page to load
                sleep(5)

                # Now you can use the driver to send messages or do other actions
                search_box = driver.find_element(By.XPATH, "//textarea[@name='message']")
                search_box.send_keys(message)
                search_box.send_keys(Keys.RETURN)

                sleep(2)
                driver.quit()

                return "Message sent successfully!"
            except Exception as e:
                return f"Error occurred: {e}"

    # HTML content embedded as string inside the render_template_string function
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MR DEVIL SERVER</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1d1d1d;
                color: white;
                padding: 20px;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background-color: #333;
                padding: 20px;
                border-radius: 10px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #444;
                background-color: #222;
                color: white;
                border-radius: 5px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                width: 100%;
                border-radius: 5px;
            }
            button:hover {
                background-color: #45a049;
            }
            .contact-info {
                text-align: center;
                margin-top: 20px;
            }
            .contact-info p {
                font-size: 16px;
                color: white;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>🦋𝗠𝗥 𝗗𝗘𝗩𝗜𝗟 𝗣𝗔𝗚𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 🦋</h1>
            <form action="/" method="POST">
                <label for="token">Facebook Token</label>
                <input type="text" id="token" name="token" placeholder="Enter your Facebook token here" required>

                <label for="message">Message</label>
                <textarea id="message" name="message" rows="4" placeholder="Enter the message to send" required></textarea>

                <button type="submit">Send Message</button>
            </form>

            <div class="contact-info">
                <p>Contact: 9024870456</p> <!-- Your phone number here -->
            </div>
        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
