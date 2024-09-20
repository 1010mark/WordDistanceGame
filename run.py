from app.app import app
print("starting...")
if __name__ == "__main__":
    port = 5000
    app.run(port=port, host="0.0.0.0")
    print(f'running on {port}')