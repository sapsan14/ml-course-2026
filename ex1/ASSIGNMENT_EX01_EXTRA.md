# EX01-EXTRA — Data analysis with Pandas (advanced, optional)

**Completion requirements**  
Opened: Saturday, 7 February 2026, 12:00 AM  
Due: Sunday, 22 February 2026, 11:59 PM  

This is an optional assignment for advanced students.

**Note:** This task has **no autotests**. Read the instructions and submit a link to your Jupyter Notebook in the “Submission” field.

## Contents

- [Objective](#objective)
- [Dataset](#dataset)
- [Task](#task)
- [Optional extra questions](#optional-extra-questions)
- [Submission](#submission)

---

## Objective

Practice Pandas on a realistic dataset and develop the ability to make meaningful conclusions from data. This task is intended for students who already know the Pandas basics covered in lectures and sample notebooks.

## Dataset

Use the dataset:

**IBM HR Analytics Employee Attrition & Performance**  
Link: [https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

The dataset contains information about employee demographics, working conditions, salary, satisfaction, and tenure.

**Note:** A free Kaggle account is required.

---

## Task

### 1) Load and inspect the data

- Load the dataset into Pandas.
- Check:
  - dataset shape (rows and columns),
  - column data types,
  - missing values.
- Briefly describe:
  - what kind of problem this is,
  - which column could be an interesting analysis target (e.g., attrition, salary, satisfaction).

### 2) Data preparation

- Split columns into logical groups:
  - numerical,
  - categorical.
- Do at least one justified preprocessing step, for example:
  - remove a constant column,
  - convert a categorical column,
  - create a derived feature (e.g., age or tenure group).
- Briefly explain why this step is necessary or useful.

### 3) Data analysis

Answer at least **three** of the following questions (you may also formulate your own):

- Do employees who left the company differ in salary or satisfaction?
- Which departments or job roles have the highest attrition rate?
- How are employee tenure and salary related?
- Is OverTime related to attrition?

Use in your analysis:

- `groupby`,
- aggregate functions (`mean`, `median`, `count`),
- sorting and filtering.

### 4) Summary

Write a short textual summary:

- 2–3 key observations,
- which features seem the most informative,
- what kind of machine learning problem could be solved with this dataset.

---

## Optional extra questions

These are not required but allow deeper analysis:

- Calculate and compare attrition rates for different age or tenure groups.
- Check whether median satisfaction differs notably between departments.
- Find features with the most different distributions for employees who left vs. stayed.
- Propose 3 features you would use in a machine learning model and justify your choice.

---

## Submission

Submit a **Jupyter Notebook (.ipynb) link**.

The notebook must include:

- code,
- short text explanations (Markdown),
- answers to the questions written as Markdown cells.
