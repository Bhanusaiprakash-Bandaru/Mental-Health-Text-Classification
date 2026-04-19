![NLP](https://img.shields.io/badge/NLP-Text%20Classification-blue)
![Model](https://img.shields.io/badge/Model-FastText-green)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit-orange)
![Type](https://img.shields.io/badge/Type-Machine%20Learning-purple)
![Dataset](https://img.shields.io/badge/Dataset-Mental%20Health-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---
# 🧠 Mental Health Text Classification

An NLP-based machine learning project that classifies user text into:
**Anxiety, Depression, Suicidal, and Normal**

---

## 🚀 Overview

This project builds an end-to-end pipeline for mental health text classification.  
It processes user input and predicts the emotional category using a FastText model.

---

## ⚙️ Tech Stack

- Python  
- FastText  
- Streamlit  
- Pandas  
- Scikit-learn  

---

## 🔄 Workflow

1. Data preprocessing (cleaning, normalization)  
2. Convert dataset to FastText format  
3. Train-test split  
4. Model training using FastText (`loss='ova'`)  
5. Model evaluation (confusion matrix, classification report)  
6. Deployment using Streamlit  

---

## 📊 Model Performance

- Works well for clear and strong emotional signals  
- Handles multi-class classification effectively  
- Achieves good accuracy on test data  

---

## ⚠️ Limitations

- Struggles with ambiguous inputs  
- Overlapping words across categories cause confusion  
- FastText has limited contextual understanding  
- Keyword bias (e.g., "lonely", "tired")  

---

## 💡 Key Learnings

- Real-world NLP data contains overlapping patterns  
- Model choice impacts contextual understanding  
- Importance of handling low-confidence predictions  
- Trade-off between speed (FastText) and accuracy (advanced models)  

---

## 🔮 Future Improvements

- Use transformer-based models (BERT, DistilBERT)  
- Improve dataset quality and labeling  
- Implement multi-label classification  
- Add more advanced preprocessing techniques  

---


## 🙏 Acknowledgment

Grateful to my guide Nagaraju Ekkirala and mentor Mohammad Afroz, and to Innomatics Research Labs for continuously shaping my learning journey in AI and deep learning.  

Special thanks to Raghu Ram Aduri, Sigilipelli Yeshwanth, and Kanav Bansal for their support and contributions.

---

## 📌 Conclusion

This project demonstrates a practical NLP application using machine learning, highlighting real-world challenges like ambiguous data, overlapping language patterns, and model limitations.
