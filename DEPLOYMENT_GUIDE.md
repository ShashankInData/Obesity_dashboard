# Deployment Guide - India Obesity Dashboard

Your dashboard is a **static HTML file** - it doesn't need a server! This makes deployment very easy and free.

## Option 1: GitHub Pages (Recommended - FREE)

### Advantages:
- ✅ Completely free
- ✅ Fast global CDN
- ✅ Easy to update
- ✅ Professional URL: `yourusername.github.io/obesity-dashboard`
- ✅ Version control included

### Steps:

1. **Create a GitHub account** (if you don't have one)
   - Go to https://github.com
   - Sign up for free

2. **Create a new repository**
   - Click "New repository"
   - Name it: `obesity-dashboard`
   - Make it Public
   - Click "Create repository"

3. **Upload your files**

   Option A - Using GitHub Desktop (Easier):
   ```
   1. Download GitHub Desktop: https://desktop.github.com/
   2. Clone your new repository
   3. Copy these files into the repository folder:
      - obesity_dashboard_enhanced.html (rename to index.html)
      - obesity_data_cleaned.csv
   4. Commit and push
   ```

   Option B - Using Git Command Line:
   ```bash
   cd C:\Users\Poorna\Desktop\obesity
   git init
   git add obesity_dashboard_enhanced.html obesity_data_cleaned.csv
   git commit -m "Initial dashboard"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/obesity-dashboard.git
   git push -u origin main
   ```

4. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "Pages" section
   - Source: Select "main" branch
   - Click Save

5. **Rename your main file**
   - Rename `obesity_dashboard_enhanced.html` to `index.html`
   - This makes it load automatically

6. **Access your dashboard**
   - URL: `https://YOUR_USERNAME.github.io/obesity-dashboard/`
   - Takes 2-3 minutes to deploy

### Update Process:
```bash
# Make changes to your files
git add .
git commit -m "Updated dashboard"
git push
# Wait 1-2 minutes for changes to appear
```

---

## Option 2: Netlify (Easiest - FREE)

### Advantages:
- ✅ Completely free
- ✅ No coding needed
- ✅ Drag and drop deployment
- ✅ Custom domain support
- ✅ Instant updates

### Steps:

1. **Go to Netlify**
   - Visit https://www.netlify.com/
   - Click "Sign up" (use GitHub account)

2. **Deploy your site**
   - Click "Add new site" → "Deploy manually"
   - Drag and drop your folder containing:
     - obesity_dashboard_enhanced.html (rename to index.html)
     - obesity_data_cleaned.csv
   - Click "Deploy"

3. **Access your dashboard**
   - Netlify gives you a URL like: `random-name-123.netlify.app`
   - You can change it to: `obesity-india.netlify.app`

4. **Update Process**
   - Just drag and drop updated files again
   - Or connect to GitHub for automatic deploys

---

## Option 3: Vercel (FREE)

### Advantages:
- ✅ Free
- ✅ Very fast
- ✅ Custom domains
- ✅ GitHub integration

### Steps:

1. Go to https://vercel.com/
2. Sign up with GitHub
3. Click "Add New" → "Project"
4. Import your GitHub repository
5. Click Deploy

---

## Option 4: Local Network Sharing (Quick Test)

### For testing with friends/colleagues on same WiFi:

```bash
# Using Python
cd C:\Users\Poorna\Desktop\obesity
python -m http.server 8000
```

Then share: `http://YOUR_IP_ADDRESS:8000/obesity_dashboard_enhanced.html`

---

## My Recommendation: GitHub Pages

**Why?**
1. Free forever
2. Professional URL
3. Version control (track changes)
4. Easy to share
5. Portfolio piece

**Quick Start (5 minutes):**
1. Create GitHub account
2. Create repository called `obesity-dashboard`
3. Upload `obesity_dashboard_enhanced.html` renamed to `index.html`
4. Enable GitHub Pages in settings
5. Done! Share the link

---

## Pre-Deployment Checklist

Before deploying, make sure you have:

- [x] `obesity_dashboard_enhanced.html` (your main file)
- [x] Rename it to `index.html` for GitHub Pages/Netlify
- [x] All charts are working (test locally first)
- [x] BMI calculator works
- [x] Educational materials are accessible (optional)

---

## Files to Deploy

### Essential (must include):
- `index.html` (renamed from obesity_dashboard_enhanced.html)

### Optional (for reference):
- `obesity_data_cleaned.csv` (already embedded in HTML, but good to include)
- `README.md` (project description)
- `patient_handout.txt` (educational materials)
- `doctor_screening_protocol.txt` (clinical guidelines)
- `social_media_campaigns.txt` (campaign messages)

---

## Custom Domain (Optional)

If you want a professional domain like `obesityindia.com`:

1. Buy a domain from:
   - Namecheap (~$10/year)
   - Google Domains (~$12/year)
   - GoDaddy (~$15/year)

2. Point it to your GitHub Pages/Netlify/Vercel site
   - They all have free SSL certificates
   - Instructions provided by each platform

---

## Troubleshooting

### Charts not showing?
- Make sure Plotly CDN is loading: `https://cdn.plot.ly/plotly-2.27.0.min.js`
- Check browser console for errors (F12)

### File not found?
- Ensure `index.html` is in the root directory
- File names are case-sensitive on some platforms

### Slow loading?
- The HTML file is ~200KB - should load in 1-2 seconds
- Charts render client-side (in user's browser)

---

## Analytics (Optional)

Track visitors with Google Analytics:

1. Create Google Analytics account
2. Get tracking code
3. Add to `<head>` section of `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-ID');
</script>
```

---

## Next Steps After Deployment

1. **Share your dashboard:**
   - Post on LinkedIn
   - Share with healthcare professionals
   - Submit to public health organizations

2. **Get feedback:**
   - Ask users what's confusing
   - Track which charts get most attention
   - Iterate and improve

3. **Keep it updated:**
   - Add new survey data when available
   - Update educational materials based on feedback
   - Add new features based on user requests

---

## Security Notes

✅ Safe to deploy:
- Static HTML/CSS/JavaScript
- No server-side code
- No user data collected
- No database

Your dashboard is completely safe and private!

---

## Support

Need help deploying?
- GitHub Pages docs: https://pages.github.com/
- Netlify docs: https://docs.netlify.com/
- Vercel docs: https://vercel.com/docs

---

**Recommended Path:**
1. Start with GitHub Pages (free, permanent)
2. Add custom domain later if needed
3. Set up analytics to see usage
4. Share widely!

Your dashboard is ready to help educate India about obesity! 🎉
