from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Flask</h1>
    <p>Use <a href=\"/hello/Student\">/hello/&lt;name&gt;</a> to see a greeting.</p>
    <p>Visit <a href=\"/contact\">/contact</a> to send a message.</p>
    """

@app.route("/hello/<name>")
def hello(name):
    # Return a personalized greeting for the visitor.
    return f"<h1>Hello, {name}!</h1><p>Welcome to your Flask app.</p>"

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        visitor_name = request.form.get("name", "Guest")
        message = request.form.get("message", "No message provided.")
        return f"<h1>Thanks, {visitor_name}!</h1><p>Your message: {message}</p>"

    return """
    <h1>Contact Form</h1>
    <form method=\"post\">
      <label>Name:<br><input name=\"name\" type=\"text\"></label><br><br>
      <label>Message:<br><textarea name=\"message\"></textarea></label><br><br>
      <button type=\"submit\">Send Message</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
