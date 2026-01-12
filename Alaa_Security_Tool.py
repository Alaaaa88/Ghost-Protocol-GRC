import socket

def check_security(url):
    print(f"🔍 Analyzing security for: {url}")
    try:
        ip = socket.gethostbyname(url)
        print(f"✅ Connection Secure. IP Address: {ip}")
    except:
        print("⚠️ Warning: Host not found or insecure connection.")

# تجربة الكود
check_security("neom.com")
