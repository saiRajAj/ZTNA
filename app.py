from flask import Flask, request
import jwt
import datetime
import platform

app = Flask(__name__)
app.config["SECRET_KEY"] = "ztna-secret-key"

USERS = {
    "admin": "password123",
    "user": "user123"
}

JWT_SECRET = "ztna-jwt-secret"
JWT_ALGO = "HS256"

def device_check():
    return platform.system() == "Darwin"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if USERS.get(username) == password:
            token = jwt.encode(
                {
                    "user": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                },
                JWT_SECRET,
                algorithm=JWT_ALGO
            )

            return f"""
            <h2>Login Successful</h2>
            <a href="/dashboard?token={token}">Go to Dashboard</a>
            """

        return "Access Denied", 403

    return """
    <h2>ZTNA Login</h2>
    <form method="post">
        Username: <input name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route("/dashboard")
def dashboard():
    token = request.args.get("token")
    if not token:
        return "Token Missing", 403

    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except Exception as e:
        return f"JWT Error: {str(e)}", 403

    if not device_check():
        return "Device Not Trusted", 403

    return f"""
    <h2>ZTNA Protected Application</h2>
    <p>User: <b>{decoded['user']}</b></p>
    <p>Device: macOS</p>
    <p>Status: Zero Trust Access Granted</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
