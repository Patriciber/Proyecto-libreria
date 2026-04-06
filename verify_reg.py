import httpx
import json

BASE_URL = "http://127.0.0.1:8005/api/auth"

def test_registration_and_login():
    client = httpx.Client()
    
    # 1. Register a new user
    print("Testing Registration...")
    reg_data = {
        "username": "testuser_new",
        "email": "newuser@example.com",
        "password": "strongpassword123",
        "full_name": "New Test User"
    }
    try:
        response = client.post(f"{BASE_URL}/register", json=reg_data)
        print(f"Registration Status: {response.status_code}")
        print(f"Registration Body: {response.text}")
        if response.status_code != 201:
            return
    except Exception as e:
        print(f"Registration Failed: {e}")
        return

    # 2. Login with the new user
    print("\nTesting Login...")
    login_data = {
        "username": reg_data["username"],
        "password": reg_data["password"]
    }
    try:
        # FastAPI OAuth2PasswordRequestForm expects form data
        response = client.post(f"{BASE_URL}/token", data=login_data)
        print(f"Login Status: {response.status_code}")
        print(f"Login Body: {response.text}")
        if response.status_code == 200:
            print("\nSUCCESS: Registration and Login work perfectly!")
        else:
            print("\nFAILURE: Login failed after successful registration.")
    except Exception as e:
        print(f"Login Failed: {e}")

if __name__ == "__main__":
    test_registration_and_login()
