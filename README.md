# ZTNA
Zero Trust Network Access (ZTNA) is a security model based on the principle “never trust, always verify.” Unlike traditional perimeter-based security, ZTNA assumes that no user, device, or application is trusted by default, whether inside or outside the network.

ZTNA provides secure, identity- and context-based access to applications instead of granting broad network access. Users connect only to specific applications they are authorized to use, not to the entire network.

#How ZTNA Works (Flow)
User requests access to an application
ZTNA controller authenticates the user (MFA, IAM)
Device security posture is verified
Policy engine evaluates access rules
Secure, encrypted connection is established only to the requested app


Step 1: Verify Python
/opt/homebrew/bin/python3 --version
You should see Python 3.13+ / 3.14+

Step 2: Create Project Folder
mkdir ~/Documents/ztna-app
cd ~/Documents/ztna-app

Step 3: Create Virtual Environment (VERY IMPORTANT)
This avoids all dependency errors.
/opt/homebrew/bin/python3 -m venv venv


Activate it:
source venv/bin/activate
✅ Your prompt must show:
(venv) r**@S***ajs-Ma***ok-*** ztna-app %

Step 4: Install Required Packages
pip install flask pyjwt

Verify:
pip list
You must see:
Flask
PyJWT

Step 5: Create app.py
nano app.py


📌 PHASE 3: Run & Test Locally
Step 6: Start Flask Server
python app.py
You should see:
Running on http://127.0.0.1:5000

Step 7: Test in Browser
Open:
http://127.0.0.1:5000

Login:
Username: admin
Password: password123

Step 8: Install Cloudflare Tunnel
brew install cloudflare/cloudflare/cloudflared


Verify:
cloudflared --version

Step 9: Start Cloudflare Quick Tunnel
Open new terminal tab:
cloudflared tunnel --url http://localhost:5000

You will see:
https://random-name.trycloudflare.com
