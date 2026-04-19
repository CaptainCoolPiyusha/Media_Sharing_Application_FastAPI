from fastapi import FastAPI, HTTPException
from app.schemas import postCreate

myapp = FastAPI()

text_posts = {
    1: {"title": "I'm the best", "content": "Just finished my first FastAPI project!"},
    2: {"title": "Learning FastAPI is fun", "content": "FastAPI makes building APIs incredibly simple and efficient."},
    3: {"title": "Python is awesome", "content": "Python's simplicity and power make it the perfect language for beginners and experts alike."},
    4: {"title": "Building scalable APIs", "content": "Tips for designing APIs that can handle millions of requests."},
    5: {"title": "Web development best practices", "content": "Always follow SOLID principles and maintain clean code structure."},
    6: {"title": "Code review tips for developers", "content": "Constructive feedback and thorough testing leads to better software."},
    7: {"title": "JavaScript vs Python comparison", "content": "Python excels in backend, JavaScript in frontend. Both have their strengths."},
    8: {"title": "Database design matters", "content": "Proper indexing and schema design can improve performance by 10x."},
    9: {"title": "Testing is crucial for quality", "content": "Unit tests, integration tests, and end-to-end tests catch bugs early."},
    10: {"title": "DevOps for beginners", "content": "Understanding deployment pipelines and CI/CD is essential for modern development."}
}

@myapp.get("/posts")
# Query-parameter
def posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]    
    return text_posts

# Path-parameter
@myapp.get("/posts/{id}")
def post_by_id(id: int):
    if id not in text_posts:
        raise HTTPException(status_code = 404, error = "Post not found")
    return text_posts.get(id)

@myapp.post("/posts")
def create_post(post: postCreate):
    new_post = {"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post