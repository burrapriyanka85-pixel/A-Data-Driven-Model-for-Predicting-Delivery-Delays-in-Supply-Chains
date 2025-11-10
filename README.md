# 📦 A Data-Driven Model for Predicting Delivery Delays in Supply Chains
**Author:** Priyanka Burra  
**Course:** M.Sc. Bioinformatics  
**Project Type:** Final Year Research Project  

---

## 🧠 Overview
This project presents a **data-driven machine learning framework** for analyzing and predicting **delivery delays** in supply chain operations.  
By leveraging data analytics and predictive modeling, the study identifies key operational and logistical factors that influence shipment delays, enabling organizations to improve efficiency, optimize processes, and enhance customer satisfaction.

---

## 🎯 Objectives
- Perform **Exploratory Data Analysis (EDA)** to uncover patterns in supply chain data.  
- Identify **key determinants** of delivery delays.  
- Build and evaluate **supervised machine learning models** for delay prediction.  
- Provide **data-driven insights** to optimize logistics and decision-making.  

---

## 📊 Dataset Information
- **Dataset Name:** DataCo Supply Chain Dataset  
- **Source:** Publicly available dataset containing order, shipment, and customer details.  
- **Path:** `data/raw/DataCoSupplyChain.csv`  

**Key Features Analyzed:**
- Shipping Mode  
- Order Processing Time  
- Delivery Status  
- Customer Segment  
- Product Category  
- Profit, Cost, and Discount Metrics  
> ⚠️ *Note:* Dataset used strictly for research and academic purposes.

---

## ⚙️ Methodology
### 1️⃣ Data Preprocessing
- Handled missing values and outliers.  
- Encoded categorical features using OneHotEncoder.  
- Normalized and transformed numeric variables for better model performance.

### 2️⃣ Exploratory Data Analysis (EDA)
- Visualized delay patterns and distributions.  
- Performed correlation and feature importance analysis.  
- Identified dependencies between shipping mode, product type, and delivery time.

### 3️⃣ Model Development
Implemented and compared multiple supervised learning models:
- **Logistic Regression**  
- **Decision Tree Classifier**  
- **Random Forest Classifier**

### 4️⃣ Model Evaluation
Evaluated models using:
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC–AUC Curve  

### 5️⃣ Deployment (Optional)
A **Streamlit-based web application** was designed to provide interactive predictions on parcel delivery delays.

---

## 🧮 Results & Discussion
- The **Random Forest Classifier** achieved the best overall accuracy for delay prediction.  
- **Shipping mode**, **handling time**, and **warehouse distance** were identified as dominant features.  
- The study highlights how **machine learning can proactively improve supply chain reliability**.

---

## 💻 Project Setup & Execution
### Step 1: Clone the Repository
```bash
git clone https://github.com/burrapriyanka85-pixel/A-Data-Driven-Model-for-Predicting-Delivery-Delays-in-Supply-Chains.git
cd A-Data-Driven-Model-for-Predicting-Delivery-Delays-in-Supply-Chains

Step 2: Install Required Dependencies
pip install -r requirements.txt

Step 3: Launch Jupyter Notebook
jupyter notebook

Step 4: Run the Analysis
Open and execute:
notebook/supply_chain_delay_analysis.ipynb

🚀 Streamlit App (Optional Demo)
To interact with the trained model through a web interface:
pip install -r requirements.txt
streamlit run app.py
Once started, open the displayed URL (typically http://localhost:8501) in your browser.

🧰 Tools & Technologies
Category	Tools / Libraries
Programming Language	Python
Libraries	Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
IDE / Environment	Jupyter Notebook
Deployment (Optional)	Streamlit
Version Control	Git, GitHub

🔮 Future Scope
Integrate deep learning models for enhanced predictive accuracy.
Include real-time IoT logistics data for continuous monitoring.
Build an interactive dashboard for supply chain performance tracking.

🙏 Acknowledgment
This research project was conducted as part of the M.Sc. Bioinformatics curriculum under faculty supervision.
All datasets and reference materials were utilized exclusively for educational and research purposes.

📜 License
This project is distributed under the MIT License.
You are free to use, modify, and distribute this work with appropriate attribution to the author.
