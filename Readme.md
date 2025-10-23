#  IBM Machine Learning with Python & Scikit-learn Capstone Projects

This repository contains notebooks I completed (using the course_ratings.csv dataset) as part of the "IBM Machine Learning with Python & Scikit-learn" course.  

## Attribution
- IBM provided starter code, datasets, and notebook structure.  
- I implemented the missing parts, completed the solutions, trained the models, and added my own explanations/visualizations.  
- All rights to the original starter code belong to IBM.  

---

# **Course Recommendation System**

This repository contains a comprehensive **Course Recommendation System** built using Python, NLP, and deep learning techniques. The system provides personalized course recommendations based on **course content**, **user profiles**, and **historical ratings**.

---

## **Project Overview**

The project demonstrates a complete recommendation pipeline combining multiple techniques:

1. **Collaborative Filtering** – Predicts user preferences based on similar users and course ratings.
2. **Content-Based Filtering** – Uses course titles, descriptions, and genres to recommend related courses.
3. **Text Analysis with Bag-of-Words (BoW)** – Extracts meaningful features from course content.
4. **Course Similarity Computation** – Measures similarity between courses using cosine similarity on BoW vectors.
5. **Neural Collaborative Filtering (NCF)** – Deep learning-based recommender model predicting user ratings for unseen courses.

Key benefits of this system:

* Personalized recommendations for each user
* Discovery of similar courses based on content
* Integration of classical and deep learning-based recommendation techniques

---

## **Repository Structure**

| Notebook                                               | Description                                                                                                                                                    |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1-lab_jupyter_cf_classification_w_embeddings.ipynb** | Collaborative filtering using embeddings with classification techniques for course recommendation.                                                             |
| **2-lab_jupyter_cf_knn.ipynb**                         | K-Nearest Neighbors (KNN) based collaborative filtering to find similar users or courses.                                                                      |
| **3-lab_jupyter_cf_nmf.ipynb**                         | Non-negative Matrix Factorization (NMF) for collaborative filtering and latent feature extraction.                                                             |
| **4-lab_jupyter_content_clustering.ipynb**             | Clustering courses based on content and features to identify groups of related courses.                                                                        |
| **5-lab_jupyter_content_course_similarity.ipynb**      | Measures similarity between courses using content features and visualizes similarity matrices.                                                                 |
| **6-lab_jupyter_content_user_profile.ipynb**           | Builds user profiles based on course interactions and genre preferences for personalized recommendations.                                                      |
| **7-lab_jupyter_eda.ipynb**                            | Exploratory Data Analysis (EDA) on courses and ratings. Includes visualizations for course popularity, user activity, and genre distributions.                 |
| **8-lab_jupyter_fe_bow_solution.ipynb**                | Feature engineering using Bag-of-Words (BoW). Includes tokenization, stop-word removal, POS tagging, and dictionary creation.                                  |
| **9-lab_jupyter_fe_course_sim.ipynb**                  | Computes course similarity using BoW features and cosine similarity. Identifies courses related to a target course.                                            |
| **10-neural_collaborative_filtering.ipynb**            | Neural Collaborative Filtering (NCF) using PyTorch. Trains a deep learning recommender, evaluates predictions, and visualizes training and prediction results. |

fix_notebooks.py is for GitHub to render the files better and more clearly
---

## **Key Features**

* **Collaborative Filtering:** KNN, embeddings, and NMF-based user-course recommendation
* **Content-Based Recommendations:** Course features, genres, and textual descriptions
* **Bag-of-Words Representation:** Tokenization, POS filtering, and vectorization
* **Similarity Measures:** Cosine similarity to find related courses
* **Neural Collaborative Filtering:** Deep learning recommender using user and course embeddings
* **Visual Analytics:** Plots for rating distributions, course popularity, training loss, and prediction errors
* **Extensible Framework:** Easily extendable to new datasets or recommendation methods

---

## **Installation & Setup**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/course-recommendation-system.git
cd course-recommendation-system
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```



4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## **Usage**

1. Open and run notebooks in the **correct order** to reproduce the full workflow:

   1. Collaborative filtering (Notebooks 1–3)
   2. Content analysis and clustering (Notebooks 4–6)
   3. Exploratory Data Analysis (Notebook 7)
   4. BoW feature engineering and course similarity (Notebooks 8–9)
   5. Neural Collaborative Filtering (Notebook 10)

2. Adjust hyperparameters or similarity thresholds as needed for experimentation.

3. Use the results to generate personalized course recommendations or identify similar courses.

---

## **Results**

* Users are profiled accurately using course interactions and genre preferences
* Similar courses are identified using BoW vectors and cosine similarity
* NCF model predicts unseen ratings with low RMSE
* Visualizations highlight rating distributions, course popularity, training loss, and prediction errors

---

## **Future Enhancements**

* Integrate **semantic embeddings** (Word2Vec, BERT) for richer course content representation
* Real-time recommendations with dynamic user input
* Deploy as a **web or mobile application** for interactive recommendations
* Incorporate user feedback to continuously improve recommendations



Note:These projects showcase my learning process. For self-driven original projects, please refer to my other repositories.
