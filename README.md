# Amazon Scraper

## Overview
Aamazon_scraper is a Python-based project that scrapes Amazon product data such as titles, prices, reviews, and images. It utilizes **Flask** for the backend and **BeautifulSoup** for scraping. The project also includes a frontend for querying data.

## Features
- Scrape product data from Amazon using search queries.
- Save scraped data in JSON and CSV formats.
- A Flask API to serve the scraped data.
- A React-based frontend for querying and displaying data.

## Demo
Click below to see the demo in action:

[![Amazon Scraper Demo](https://img.shields.io/badge/Demo-Click_Here-blue?style=for-the-badge&logo=appveyor)](https://github.com/engrmumtazali0112/python-script-amazon-scraper/blob/main/IMG_8363-ezgif.com-video-to-gif-converter.gif)

---
## Project Structure
```
amazon_scraper/
├── backend/
│   ├── app.py               # Flask backend application
│   ├── main.py              # Scraping runner script
│   ├── scraper.py           # Amazon scraper script
│   ├── utils.py             # Utility functions
│   ├── user_queries.json    # Input queries for scraping
│   ├── requirements.txt     # Python dependencies
│   ├── runtime.txt          # Python version for Heroku
│   ├── output/              # Folder for storing scraped data
│   └── vercel.json          # Configuration for Vercel deployment
├── frontend/
│   ├── public/              # Public files for React app
│   ├── src/                 # Source code for React app
│   ├── package.json         # Node.js dependencies
│   ├── .env                 # Environment variables
│   └── build/               # Compiled frontend files

```
# Installation and Setup

## Backend Setup
1. Clone the repository:
   ```
   git clone https://github.com/engrmumtazali0112/python-script-amazon-scrape.git
   cd amazon_scraper/backend
    ```
## Install dependencies:

 ```
pip install -r requirements.txt
 ```
2. Run the Flask server:
 ```
python app.py
 ```
3. Access the backend at http://127.0.0.1:5000.
   
# Frontend Setup
1. Navigate to the frontend folder:
 ```
cd ../frontend
 ```
2. Install Node.js dependencies:

 ```
npm install
 ```
3. Start the development server:
 ```
npm start
 ```

# Deployment
## Backend Deployment on Vercel

Ensure vercel.json is correctly configured.
## Deploy the backend:

 ```
   vercel --prod
 ```
Frontend Deployment on Vercel

Build the React app:
 ```
npm run build
 ```
Deploy the frontend:
 ```
vercel --prod
 ```
# Dependencies
- Python 3.12
- Flask
- BeautifulSoup
- React.js
- Node.js

  
# Steps to Update Your `README.md`

1. **Open Your `README.md` File** in your project directory.
2. **Replace the Existing Content** with the updated content provided above.
3. **Save the File**.

# Add, Commit, and Push Changes

After updating the `README.md`, you need to add, commit, and push the changes to your GitHub repository:

1. **Add the Changes**:
```
   git add README.md
```

# 📌 Follow Us

📜 License
This repository is licensed under the MIT License.
<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mumtaz-ali"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.instagram.com/its_maliyzi"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://x.com/mumtazali1223/status/1846913595021328672?s=51"><img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/></a>
  <a href="https://discord.gg/DZgwHzEb"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"/></a>
  <a href="https://wa.me/923476338292" target="_blank"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>
</p>

<p align="center">Made with ❤️ by Mumtaz Ali</p>

**Happy coding!** ✨
