import requests
from base64 import b64encode

# Replace these with your actual details
username = "AutoPoster"
app_password = "C0Q3 VKUN kY1j uKBw oblk qJI1"
site_url = "https://www.6club.ink"

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

# Example blog list (Replace with 5 daily posts)
blogs = [
    {"title": "AI Agent Blog 1", "content": "This blog is posted by your AI agent."},
    {"title": "AI Agent Blog 2", "content": "Fully automated. Free. Zero BS."},
    {"title": "AI Agent Blog 3", "content": "Yes, it really works."},
    {"title": "AI Agent Blog 4", "content": "You can scale it anytime."},
    {"title": "AI Agent Blog 5", "content": "Posted via GitHub Automation."}
]

for blog in blogs:
    post_blog(blog["title"], blog["content"])
