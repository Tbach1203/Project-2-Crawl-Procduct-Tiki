# 🛒 Project-2-Crawl-Product-Tiki
## 🔍 Overview
This project focuses on collecting large-scale product data from **Tiki.vn**, using a dataset of approximately **200,000** product IDs.
## 📌 Features
- Crawl data for **~200,000 Tiki product IDs** using Python  
- Save output as **JSON files chunked by ~1,000 products per file**  
- Extract and standardize key product fields:
  - `id`
  - `name`
  - `url_key`
  - `price`
  - `description`
  - `images_url` 
- Implement performance optimizations to **reduce data retrieval time**:
  - Concurrent requests
  - Request batching
  - Retry and error handling
- Modular codebase designed for scalability and maintainability   
## 📂 Project Structure
Project-2-Crawl-Product-Tiki
├── config # configuration files
├── etl # data processing & transformation
├── input # list product ID
├── product # product crawling logic
├── .gitignore
├── requirements.txt
└── README.md
