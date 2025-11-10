# 📦 A Data-Driven Model for Predicting Delivery Delays in Supply Chains
**Author:** Priyanka Burra  
**Course:** M.Sc. Bioinformatics  
**Type:** Final Year Research Project  

---

### 🔍 Project Description
A data-driven machine learning project designed to analyze and predict **delivery delays** in supply chain operations using **data analytics** and **predictive modeling techniques**.  
This project identifies patterns in real-world logistics data and provides insights to help organizations improve efficiency, reliability, and customer satisfaction.

---

## 🧠 Project Overview
In modern supply chains, timely delivery is crucial for customer retention and operational success.  
This project leverages **data science and machine learning** to predict whether a product shipment will be delayed based on various logistical, product, and customer features.  
By performing detailed **Exploratory Data Analysis (EDA)** and developing predictive models, this study aims to identify critical factors contributing to delivery delays and propose data-driven optimization strategies.

---

## 🎯 Objectives
- Perform **Exploratory Data Analysis (EDA)** on supply chain datasets.  
- Identify **key factors** influencing delivery delays.  
- Build and evaluate **machine learning models** for delay prediction.  
- Generate **actionable insights** to improve logistics performance.

---

## 🧩 Dataset
- **Dataset Name:** DataCo Supply Chain Dataset  
- **Source:** Publicly available dataset containing order, shipping, and customer details.  
- **File Path:** `data/raw/DataCoSupplyChain.csv`  

**Key Features:**
- Shipping Mode  
- Order Processing Time  
- Delivery Status  
- Customer Segment  
- Product Category  
- Profit, Cost, and Discounts  
> ⚠️ Note: The dataset is used for research and academic purposes only.

---

## 🧮 Methodology
### 🔹 1. Data Cleaning & Preprocessing
- Handling missing values and outliers  
- Encoding categorical variables  
- Normalizing and transforming data  

### 🔹 2. Exploratory Data Analysis (EDA)
- Visualizing trends and delay distributions  
- Correlation analysis of numerical features  
- Identifying relationships between shipping mode, distance, and delay  

### 🔹 3. Model Development
Implemented supervised learning algorithms:
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  

### 🔹 4. Model Evaluation
Metrics used:
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC-AUC Curve  

### 🔹 5. Deployment *(Optional)*
A **Streamlit-based web application** was created for interactive prediction of delivery delays using trained machine learning models.

---

## 📊 Results & Discussion
- The **Random Forest Classifier** achieved the **highest accuracy** in predicting delayed deliveries.  
- **Shipping mode**, **order handling time**, and **warehouse distance** were identified as the most significant factors.  
- Visual analytics helped pinpoint bottlenecks in order fulfillment and transportation processes.  
- The study demonstrates the potential of machine learning in **proactive supply chain management**.

---

## 🖥️ How to Run the Project
1. **Clone this repository**
   ```bash
   git clone https://github.com/burrapriyanka85-pixel/A-Data-Driven-Model-for-Predicting-Delivery-Delays-in-Supply-Chains.git

2. Navigate to the project directory
cd A-Data-Driven-Model-for-Predicting-Delivery-Delays-in-Supply-Chains

3. Install dependencies
pip install -r requirements.txt

4. Launch Jupyter Notebook
jupyter notebook

5. Run the analysis
Open and execute the file:
notebook/supply_chain_delay_analysis.ipynb

📈 Tools & Technologies
Category	Tools / Libraries Used
Programming Language	Python
Libraries	Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Environment	Jupyter Notebook
Visualization	Matplotlib, Seaborn
Deployment (Optional)	Streamlit

🧩 Future Scope
Implement deep learning models for higher predictive accuracy.
Integrate real-time data streams from IoT-enabled logistics systems.
Develop a business intelligence dashboard for continuous monitoring and analytics.

🙏 Acknowledgment
This project was developed as part of the M.Sc. Bioinformatics final year curriculum under faculty supervision.
The dataset and reference materials were utilized solely for academic and research purposes.

📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute it with proper attribution to the author.
