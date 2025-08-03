import os
import re
import tempfile

from flask import Flask, flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your-secret-key-change-this-in-production"

# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"bib", "txt"}

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def clean_bibliography(unused_keys_content, bib_content):
    """
    Clean bibliography by removing unused entries.

    Args:
        unused_keys_content (str): Content of the unused keys file
        bib_content (str): Content of the .bib file

    Returns:
        tuple: (cleaned_bib_content, removed_count)
    """
    # Parse unused keys
    unused_keys = set()
    for line in unused_keys_content.split("\n"):
        if line.strip().startswith("=> "):
            # Extract the key by splitting the line and taking the last word
            key = line.strip().split()[-1]
            unused_keys.add(key)

    # Filter out the unused entries
    bib_parts = bib_content.split("@")
    header = bib_parts[0]
    entries = bib_parts[1:]

    kept_entries = []
    removed_count = 0

    for entry_str in entries:
        # Use regex to find the citation key
        match = re.search(r"^\s*\w+\s*\{\s*([^,]+)", entry_str)

        if match:
            key = match.group(1).strip()
            # If the key is NOT in our unused list, we keep the entry.
            if key not in unused_keys:
                kept_entries.append("@" + entry_str)
            else:
                removed_count += 1
        else:
            # Keep malformed entries or comments to be safe.
            kept_entries.append("@" + entry_str)

    cleaned_content = header + "".join(kept_entries)
    return cleaned_content, removed_count


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    # Check if files are present
    if "bib_file" not in request.files or "unused_keys_file" not in request.files:
        flash("Please select both files")
        return redirect(url_for("index"))

    bib_file = request.files["bib_file"]
    unused_keys_file = request.files["unused_keys_file"]

    # Check if files are selected
    if bib_file.filename == "" or unused_keys_file.filename == "":
        flash("Please select both files")
        return redirect(url_for("index"))

    # Check file extensions
    if not (
        allowed_file(bib_file.filename) and allowed_file(unused_keys_file.filename)
    ):
        flash("Please upload .bib and .txt files only")
        return redirect(url_for("index"))

    try:
        # Read file contents
        bib_content = bib_file.read().decode("utf-8")
        unused_keys_content = unused_keys_file.read().decode("utf-8")

        # Process the files
        cleaned_bib, removed_count = clean_bibliography(
            unused_keys_content, bib_content
        )

        # Create a temporary file for download
        temp_file = tempfile.NamedTemporaryFile(
            mode="w", suffix="_cleaned.bib", delete=False, encoding="utf-8"
        )
        temp_file.write(cleaned_bib)
        temp_file.close()

        # Prepare result data
        result_data = {
            "removed_count": removed_count,
            "original_filename": secure_filename(bib_file.filename),
            "temp_file_path": temp_file.name,
        }

        return render_template("result.html", **result_data)

    except Exception as e:
        flash(f"Error processing files: {str(e)}")
        return redirect(url_for("index"))


@app.route("/download/<path:filename>")
def download_file(filename):
    try:
        # Security check - ensure the file is in temp directory
        if not filename.startswith("/tmp") and not filename.startswith(
            tempfile.gettempdir()
        ):
            flash("Invalid file path")
            return redirect(url_for("index"))

        return send_file(
            filename, as_attachment=True, download_name="bibliography_cleaned.bib"
        )

    except Exception as e:
        flash(f"Error downloading file: {str(e)}")
        return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # Use environment variables for production deployment
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
