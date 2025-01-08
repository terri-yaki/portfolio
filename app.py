import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "some-secret-key"  # Replace with something secure in production

DATA_FILE = "data.json"

def load_data():
    """Utility to load data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    """Utility to save data to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def home():
    """Render the portfolio main page."""
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    """
    Single admin route to handle:
    - Display (GET)
    - CRUD actions (POST)
    """
    data = load_data()

    if request.method == "POST":
        section = request.form.get("section")     # experience, project, certificate
        action = request.form.get("action")       # add, update, delete
        item_id = request.form.get("item_id")     # index (if updating or deleting)
        
        # Ensure these lists exist in data
        data.setdefault("experience", [])
        data.setdefault("projects", [])
        data.setdefault("certifications", [])

        # Handle "Add" operations
        if action == "add":
            if section == "experience":
                role = request.form.get("role", "").strip()
                company = request.form.get("company", "").strip()
                period = request.form.get("period", "").strip()
                details_raw = request.form.get("details", "")
                # Split lines
                details_list = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                new_exp = {
                    "role": role,
                    "company": company,
                    "period": period,
                    "details": details_list
                }
                data["experience"].append(new_exp)
                flash("New experience added.")

            elif section == "projects":
                title = request.form.get("title", "").strip()
                details_raw = request.form.get("details", "")
                details_list = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                new_proj = {
                    "title": title,
                    "details": details_list
                }
                data["projects"].append(new_proj)
                flash("New project added.")

            elif section == "certifications":
                cert = request.form.get("cert", "").strip()
                data["certifications"].append(cert)
                flash("New certificate added.")

            else:
                flash("Unknown section for adding.")
            
            save_data(data)

        # Handle "Update" operations
        elif action == "update":
            # item_id is required
            if item_id is None:
                flash("No item_id provided for update.")
                return redirect(url_for("admin"))

            idx = int(item_id)
            if section == "experience":
                if 0 <= idx < len(data["experience"]):
                    role = request.form.get("role", "").strip()
                    company = request.form.get("company", "").strip()
                    period = request.form.get("period", "").strip()
                    details_raw = request.form.get("details", "")
                    details_list = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                    data["experience"][idx] = {
                        "role": role,
                        "company": company,
                        "period": period,
                        "details": details_list
                    }
                    flash("Experience updated.")
                else:
                    flash("Invalid experience index.")

            elif section == "projects":
                if 0 <= idx < len(data["projects"]):
                    title = request.form.get("title", "").strip()
                    details_raw = request.form.get("details", "")
                    details_list = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                    data["projects"][idx] = {
                        "title": title,
                        "details": details_list
                    }
                    flash("Project updated.")
                else:
                    flash("Invalid project index.")

            elif section == "certifications":
                certs = data["certifications"]
                if 0 <= idx < len(certs):
                    new_cert = request.form.get("cert", "").strip()
                    certs[idx] = new_cert
                    flash("Certificate updated.")
                else:
                    flash("Invalid certificate index.")

            else:
                flash("Unknown section for updating.")

            save_data(data)

        # Handle "Delete" operations
        elif action == "delete":
            if item_id is None:
                flash("No item_id provided for delete.")
                return redirect(url_for("admin"))
            
            idx = int(item_id)
            if section == "experience":
                if 0 <= idx < len(data["experience"]):
                    data["experience"].pop(idx)
                    flash("Experience deleted.")
                else:
                    flash("Invalid experience index.")

            elif section == "projects":
                if 0 <= idx < len(data["projects"]):
                    data["projects"].pop(idx)
                    flash("Project deleted.")
                else:
                    flash("Invalid project index.")

            elif section == "certifications":
                if 0 <= idx < len(data["certifications"]):
                    data["certifications"].pop(idx)
                    flash("Certificate deleted.")
                else:
                    flash("Invalid certificate index.")

            else:
                flash("Unknown section for deleting.")

            save_data(data)

        else:
            flash("Unknown action.")

        return redirect(url_for("admin"))

    # If GET, just display admin page
    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
