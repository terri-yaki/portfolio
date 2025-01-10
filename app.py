# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    """Utility to load data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    """Utility to save data to the JSON file."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

# Admin page to handle CRUD operations
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    data = load_data()
    if request.method == 'POST':
        section = request.form.get('section')
        action = request.form.get('action')
        item_id = request.form.get('item_id')

        # Ensure sections exist
        data.setdefault('experience', [])
        data.setdefault('projects', [])
        data.setdefault('certifications', [])

        if action == 'add':
            if section == 'experience':
                role = request.form.get('role')
                company = request.form.get('company')
                period = request.form.get('period')
                details_raw = request.form.get('details', '')
                details = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                new_experience = {
                    "role": role,
                    "company": company,
                    "period": period,
                    "details": details
                }
                data["experience"].append(new_experience)
                flash("New experience added!")

            elif section == 'project':
                title = request.form.get('title')
                details_raw = request.form.get('details', '')
                details = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                new_project = {
                    "title": title,
                    "details": details
                }
                data["projects"].append(new_project)
                flash("New project added!")

            elif section == 'certifications':
                cert = request.form.get('cert')
                data["certifications"].append(cert)
                flash("New certificate added!")

        elif action == 'update':
            if not item_id:
                flash("No item_id provided for update.")
                return redirect(url_for('admin'))
            idx = int(item_id)

            if section == 'experience':
                if 0 <= idx < len(data["experience"]):
                    role = request.form.get('role')
                    company = request.form.get('company')
                    period = request.form.get('period')
                    details_raw = request.form.get('details', '')
                    details = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                    data["experience"][idx] = {
                        "role": role,
                        "company": company,
                        "period": period,
                        "details": details
                    }
                    flash("Experience updated!")
                else:
                    flash("Invalid experience index.")

            elif section == 'project':
                if 0 <= idx < len(data["projects"]):
                    title = request.form.get('title')
                    details_raw = request.form.get('details', '')
                    details = [line.strip("-• \n\r\t") for line in details_raw.splitlines() if line.strip()]

                    data["projects"][idx] = {
                        "title": title,
                        "details": details
                    }
                    flash("Project updated!")
                else:
                    flash("Invalid project index.")

            elif section == 'certifications':
                if 0 <= idx < len(data["certifications"]):
                    cert = request.form.get('cert')
                    data["certifications"][idx] = cert
                    flash("Certificate updated!")
                else:
                    flash("Invalid certificate index.")

        elif action == 'delete':
            if not item_id:
                flash("No item_id provided for delete.")
                return redirect(url_for('admin'))
            idx = int(item_id)

            if section == 'experience':
                if 0 <= idx < len(data["experience"]):
                    data["experience"].pop(idx)
                    flash("Experience deleted!")
                else:
                    flash("Invalid experience index.")

            elif section == 'project':
                if 0 <= idx < len(data["projects"]):
                    data["projects"].pop(idx)
                    flash("Project deleted!")
                else:
                    flash("Invalid project index.")

            elif section == 'certifications':
                if 0 <= idx < len(data["certifications"]):
                    data["certifications"].pop(idx)
                    flash("Certificate deleted!")
                else:
                    flash("Invalid certificate index.")

        else:
            flash("Unknown action.")

        save_data(data)
        return redirect(url_for('admin'))

    return render_template('admin.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

# run.py
from waitress import serve
from app import app

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=1808)
