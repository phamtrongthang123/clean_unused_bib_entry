# 📚 Bibliography Cleaner - Web App

A web-based tool to clean unused citation entries from .bib files. Perfect for researchers who maintain large bibliography databases but only cite a fraction of the entries in their documents.

## 🌐 **Live Demo**

*Deploy your own instance using the instructions below!*

## ✨ **Features**

- 📁 **File Upload Interface**: Easy drag-and-drop file upload
- 🧹 **Automatic Cleaning**: Removes unused citations based on `checkcites` output
- 📥 **Instant Download**: Get your cleaned .bib file immediately
- 🎨 **Modern UI**: Clean, responsive design that works on all devices
- 🔒 **Privacy-First**: Files are processed temporarily and not stored
- 📖 **User-Friendly**: Step-by-step instructions and helpful tooltips

## 🚀 **Quick Start**

### **For Users:**
1. Run `checkcites output.aux > unused_keys.txt` on your LaTeX project
2. Visit the web app
3. Upload your .bib file and unused_keys.txt file
4. Download your cleaned bibliography!

### **For Developers:**
```bash
# Clone the repository
git clone <your-repo-url>
cd clean_unused_bib_entry

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Visit `http://localhost:5000` to use the app locally.

## 📁 **Project Structure**

```
clean_unused_bib_entry/
├── app.py                  # Main Flask application
├── checkcite_filter.py     # Original CLI script
├── requirements.txt        # Python dependencies
├── Procfile               # For deployment
├── templates/             # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Main upload page
│   ├── result.html       # Results page
│   └── about.html        # About page
├── DEPLOYMENT.md         # Deployment guide
└── README_WEBAPP.md      # This file
```

## 🛠️ **Technology Stack**

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Gunicorn WSGI server
- **Styling**: Custom CSS with gradient backgrounds

## 📋 **How It Works**

1. **Upload Phase**: Users upload two files:
   - `.bib` file: Original bibliography
   - `.txt` file: Output from `checkcites` command

2. **Processing Phase**: The app:
   - Parses the unused keys from the text file
   - Scans the .bib file for citation entries
   - Removes entries matching unused keys
   - Preserves file structure and formatting

3. **Download Phase**: Users receive:
   - Cleaned .bib file
   - Summary of removed entries
   - Option to process another file

## 🔧 **Configuration**

### **Environment Variables**
- `PORT`: Server port (default: 5000)
- `FLASK_ENV`: Environment mode (`development` or `production`)
- `SECRET_KEY`: Flask secret key (set in production)

### **File Limits**
- Supported formats: `.bib`, `.txt`
- Processing: In-memory (suitable for typical bibliography files)
- Security: Filename sanitization and type checking

## 🌍 **Deployment Options**

### 🏆 **Recommended: Render (Free)**
1. Fork this repository
2. Create account at [render.com](https://render.com)
3. Create new Web Service from GitHub
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app --host 0.0.0.0 --port $PORT`

### 🛩️ **Alternative: Fly.io**
```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Deploy
fly launch
fly deploy
```

### 📋 **Full Deployment Guide**
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on all platforms.

## 🧪 **Testing Locally**

1. **Prepare test files**:
   ```bash
   # Create a sample unused keys file
   echo "=> unused_citation_1" > test_unused.txt
   echo "=> unused_citation_2" >> test_unused.txt
   
   # Use any .bib file you have
   ```

2. **Run the app**:
   ```bash
   python app.py
   ```

3. **Test the functionality**:
   - Visit `http://localhost:5000`
   - Upload your test files
   - Verify the cleaning works correctly

## 📈 **Performance Considerations**

- **Memory Usage**: Files are processed in memory for speed
- **File Size**: Suitable for typical academic .bib files (up to several MB)
- **Concurrent Users**: Flask development server handles light concurrent usage
- **Production**: Use Gunicorn for better performance and concurrency

## 🔒 **Security Features**

- **File Type Validation**: Only allows `.bib` and `.txt` files
- **Filename Sanitization**: Prevents path traversal attacks
- **Temporary Processing**: Files are not permanently stored
- **Input Validation**: Proper error handling for malformed files

## 🐛 **Troubleshooting**

### **Common Issues:**

1. **Upload Fails**:
   - Check file extensions (.bib, .txt)
   - Ensure files are not empty
   - Verify file encoding (UTF-8 recommended)

2. **Processing Errors**:
   - Check unused keys file format (`=> key_name`)
   - Verify .bib file is well-formed
   - Check for special characters in citation keys

3. **Download Problems**:
   - Ensure browser allows file downloads
   - Check available disk space
   - Try a different browser

### **Getting Help**:
- Check the console output for error messages
- Verify input file formats match examples
- Test with smaller files first

## 🤝 **Contributing**

Contributions are welcome! Areas for improvement:

- **UI/UX**: Better file upload interface
- **Features**: Batch processing, preview mode
- **Performance**: Streaming for large files
- **Testing**: Unit tests for core functionality

## 📜 **License**

This project is open source. Feel free to use, modify, and distribute.

## 🙏 **Acknowledgments**

- Original CLI script: [checkcite_filter.py](checkcite_filter.py)
- Built for the academic community
- Inspired by the need for clean, manageable bibliography files

---

## 📞 **Support**

If you find this tool useful:
- ⭐ Star the repository
- 🐛 Report bugs in the issues section
- 💡 Suggest features and improvements
- 📢 Share with fellow researchers!

**Happy researching! 📚✨**