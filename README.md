# xss_lab.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>XSS Test Lab</h2>

    <form action="/search">
        <input name="q" placeholder="Search">
        <button type="submit">Search</button>
    </form>

    <br>

    <form method="POST" action="/comment">
        <input name="comment" placeholder="Leave comment">
        <button type="submit">Post</button>
    </form>
    """

# -----------------------------------
# REFLECTED XSS
# -----------------------------------
@app.route("/search")
def search():
    q = request.args.get("q", "")

    # VULNERABLE: user input directly rendered
    return f"""
    <h3>Search Results</h3>
    You searched for: {q}
    """

# -----------------------------------
# STORED XSS
# -----------------------------------
comments = []

@app.route("/comment", methods=["POST"])
def comment():
    text = request.form.get("comment", "")

    # VULNERABLE: storing unsanitized HTML
    comments.append(text)

    output = "<h3>Comments</h3>"

    for c in comments:
        output += f"<div>{c}</div><hr>"

    return output

if __name__ == "__main__":
    app.run(debug=True, port=5000)
