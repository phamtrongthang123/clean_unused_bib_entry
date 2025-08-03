# 🚀 Deployment Guide for Bibliography Cleaner

This guide covers how to deploy the Bibliography Cleaner web app to various free hosting platforms.

## 📋 Prerequisites

Before deploying, make sure you have:
- A GitHub account
- Your code pushed to a GitHub repository
- All files in place:
  - `app.py` (main Flask application)
  - `requirements.txt` (Python dependencies)
  - `Procfile` (for some platforms)
  - `templates/` folder with HTML files

## 🏆 **Option 1: Render (RECOMMENDED)**

Render offers an excellent free tier and is very beginner-friendly.

### Steps:
1. **Create Render Account:**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Deploy Your App:**
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub repository
   - Configure the deployment:
     - **Name:** `bibliography-cleaner` (or your choice)
     - **Language:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app --host 0.0.0.0 --port $PORT`
     - **Plan:** Free

3. **Deploy:**
   - Click **"Create Web Service"**
   - Wait for deployment (usually 2-5 minutes)
   - Your app will be live at `https://your-app-name.onrender.com`

### ✅ **Render Pros:**
- 750 free hours per month
- Auto-deploys on git push
- Custom domains supported
- Good uptime
- Easy SSL certificates

---

## 🛩️ **Option 2: Fly.io**

Fly.io offers generous free tier and global edge deployment.

### Steps:
1. **Install Fly CLI:**
   ```bash
   # On Windows (PowerShell)
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   
   # On macOS/Linux
   curl -L https://fly.io/install.sh | sh
   ```

2. **Sign Up & Login:**
   ```bash
   fly auth signup
   fly auth login
   ```

3. **Deploy:**
   ```bash
   # From your project directory
   fly launch
   # Follow the prompts - it will auto-detect Flask
   
   # Deploy
   fly deploy
   ```

### ✅ **Fly.io Pros:**
- Generous free tier
- Global edge deployment
- Fast startup times
- Good for scaling

---

## 🚂 **Option 3: Railway**

Railway provides $5 monthly credit (effectively free for small apps).

### Steps:
1. **Create Railway Account:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy:**
   - Click **"New Project"**
   - Select **"Deploy from GitHub repo"**
   - Choose your repository
   - Railway auto-detects and deploys Flask apps

### ✅ **Railway Pros:**
- $5 monthly credit
- Very simple deployment
- Good dashboard
- Auto-scaling

---

## ⚡ **Option 4: Vercel (Serverless)**

Good for lightweight applications.

### Steps:
1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Create vercel.json:**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "./app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "/"
       }
     ]
   }
   ```

3. **Deploy:**
   ```bash
   vercel --prod
   ```

---

## 🔧 **Environment Configuration**

For production deployment, consider setting these environment variables:

- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key-here`

**On Render:**
- Go to your service → Environment tab
- Add variables there

**On Fly.io:**
```bash
fly secrets set SECRET_KEY=your-secret-key-here
```

---

## 📝 **Troubleshooting**

### Common Issues:

1. **Build Fails:**
   - Check `requirements.txt` for typos
   - Ensure Python version compatibility

2. **App Won't Start:**
   - Verify the start command: `gunicorn app:app`
   - Check logs on your platform's dashboard

3. **File Upload Issues:**
   - Some platforms have file size limits
   - Current app handles files in memory (good for small files)

### **Platform-Specific Logs:**
- **Render:** Service → Logs tab
- **Fly.io:** `fly logs`
- **Railway:** Project dashboard → Deployments
- **Vercel:** Dashboard → Functions tab

---

## 🎯 **Recommendation**

For beginners: **Start with Render** - it's the most straightforward and has excellent documentation.

For advanced users: **Fly.io** offers more control and better performance.

## 🔗 **Next Steps After Deployment**

1. Test your deployed app thoroughly
2. Set up a custom domain (optional)
3. Monitor usage and performance
4. Consider setting up monitoring/alerts
5. Share your app with colleagues!

---

## 💡 **Cost Considerations**

All mentioned platforms offer free tiers suitable for moderate usage:

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| Render | 750 hours/month | General use, beginners |
| Fly.io | 3 shared-cpu VMs | Performance, scaling |
| Railway | $5 credit/month | Simple deployment |
| Vercel | Generous serverless | Lightweight apps |

Choose based on your expected traffic and technical requirements!