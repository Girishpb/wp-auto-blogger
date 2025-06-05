import requests
import os
from base64 import b64encode

username = os.environ["WP_USERNAME"]
app_password = os.environ["WP_PASSWORD"]
site_url = os.environ["WP_SITE_URL"]

auth = b64encode(f"{username}:{app_password}".encode()).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/json"
}

def post_blog(title, content):
    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    res = requests.post(f"{site_url}/wp-json/wp/v2/posts", headers=headers, json=data)
    print(res.status_code)
    print(res.text)

# Example 5 blogs
blogs = [
    {"title": "Auto Blog 1", "content": "Posted by a free AI bot."},
    {"title": "Auto Blog 2", "content": "No paid tools used."},
    {"title": "Auto Blog 3", "content": "WordPress REST API rocks."},
    {"title": "Auto Blog 4", "content": "GitHub Actions is awesome."},
    {"title": "Auto Blog 5", "content": "Yes, you can scale this easily."}
]

for blog in blogs:
    post_blog(blog["title"], blog["content"])
