from flask import Flask, request, render_template, redirect, url_for
from helpers import fetch_title, add_entry, fetch_all_entries, get_entry_by_id


app = Flask(__name__)


# Home page: Show article entries
@app.route("/", methods=["GET"])
def index():
    entries = fetch_all_entries() # fecth from db
    return render_template("index.html", entries=entries)
    

@app.route("/add", methods=["GET", "POST"])
def add_article():
     if request.method == "POST":
          form_data = request.form.to_dict()

          # fetch title dynamically
          form_data["title"] = fetch_title(form_data["url"])
          add_entry(**form_data) # unpack keys/values as arguments
          return redirect(url_for("index"))
        
     # If Get request, show the add article form
     return render_template("add.html")
        

@app.route("/details/<int:entry_id>")
def article_details(entry_id):
     entry = get_entry_by_id(entry_id)    # fetch from db
     if entry:
          # Show single article details
          return render_template("details.html", entry=entry)
     return redirect(url_for("index"))
     
    
if __name__ == "__main__":
     app.run(debug=True)