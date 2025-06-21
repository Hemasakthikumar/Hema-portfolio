from flask import Flask, request, render_template
from flask_mail import Mail, Message

# Step 1: Create the app
app = Flask(__name__)

# Step 2: Configure your email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hemasakthikumar472@gmail.com'         # 🔁 Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'rzdg kyfv ivou vede'            # 🔁 Replace with Gmail app password

mail = Mail(app)

# Step 3: Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(subject=f"Message from {name}",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['hemasakthikumar472@gmail.com'],
                  body=f"From: {name} <{email}>\n\n{message}")
    
    mail.send(msg)
    return "<h2>Thank you! Your message has been sent successfully.</h2>"

# Step 4: Run the app
if __name__ == '__main__':
    app.run(debug=True)
