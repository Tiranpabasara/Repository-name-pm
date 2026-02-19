from flask import Flask, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Supabase settings
url = "https://mzjvxvuyyksqhfkhlabf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im16anZ4dnV5eWtzcWhma2hsYWJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE1MDg2NDQsImV4cCI6MjA4NzA4NDY0NH0.xHrMlYsKvkNwpvr1GxLmf0tw2iK_TwqnS6TWXHuZpiw" 

supabase = create_client(url, key)

@app.route("/")
def home():
    return "PM Backend Running"

@app.route("/machines")
def machines():
    response = supabase.table("machines").select("*").execute()
    return jsonify(response.data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

