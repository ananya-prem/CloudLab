from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"  # Required for flash messages

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Grab data submitted from the HTML contact form
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Print the submission to your terminal (or save to a database here)
        print(f"New message from {name} ({email}): {message}")
        
        # Show a confirmation banner on the webpage
        flash(f"Thank you, {name}! Your message has been received.")
        return redirect(url_for("home"))
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

