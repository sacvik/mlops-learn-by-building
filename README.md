#  Full Stack MLOps Learning Repository

Welcome to the **MLOps Learning Lab** — a hands-on, open-source repository designed to help you **understand, build, and scale** real-world MLOps systems. This project will guide you through the **full MLOps lifecycle** using open-source tools, across multiple types of machine learning models.

---

##  What This Repo Covers

This repository is structured to help you **learn MLOps by doing**, through well-documented examples and tutorials.

### 🧠 1. **Introduction to MLOps**

MLOps (Machine Learning Operations) is the discipline of automating, monitoring, and scaling ML systems in production. It combines the principles of:
- **DevOps** (for CI/CD, versioning, testing)
- **ML engineering** (for experimentation, training, model management)
- **Data engineering** (for reproducibility, orchestration, pipelines)

> ⚙️ This repo breaks MLOps into simple, actionable components using **open-source tools** like:
- `MLflow` for experiment tracking
- `DVC` for data versioning
- `Prefect`/`Airflow` for pipeline orchestration
- `FastAPI` for deployment
- `Evidently AI` for monitoring
- `Docker` for environment management

---

### 📘 2. **This Is a Learning Repository**

This repository is **not just code**. It's a full-fledged learning environment. You will find:
- 📚 Step-by-step **tutorials and guides**
- 📂 Organized **project directories** for each ML use case
- 📈 Working **pipelines and dashboards** for experimentation and monitoring
- ✅ Checklists and best practices to reinforce learning

Each project is designed to help you learn the **why, what, and how** of MLOps components with practical examples.

---

### 🔁 3. **Tutorials for Each MLOps Component**

For every MLOps module, you will find a dedicated tutorial:
| MLOps Component      | Covered in Repo                        | Guide/Tutorial   | Topics Covered                          |
|----------------------|----------------------------------------|------------------|------------------------------------------|
| Data Versioning      | `DVC` based in `data/`               | Coming Soon   | Raw/processed data tracking, storage, reproducibility** |
| Orchestration        | `Prefect`/`Airflow` pipelines        |  Coming Soon   | Task scheduling, data pipeline management, error handling |
| Model Training       |  Structured + BERT examples           |  Coming Soon   | Training scripts, config-based runs, HuggingFace/Baseline models |
| Experiment Tracking  | `MLflow` integrated in pipelines     |  Coming Soon   | Run tracking, hyperparameter logging, model comparison |
| CI/CD                | GitHub Actions workflows             |  Coming Soon   | Test automation, linting, pipeline validation, deployment triggers |
| Serving APIs         | `FastAPI` deployments                |  Coming Soon   | Model packaging, REST API endpoints, Dockerization |
| Monitoring           | Drift detection with `Evidently`     |  Coming Soon   | Feature distribution monitoring, alerting, dashboarding |


> As you go deeper, you'll be able to compare different tools and designs using **two end-to-end projects**:
- `structured_model/` → Tabular ML (e.g., classification/regression)
- `text_model/` → NLP pipeline (e.g., BERT fine-tuning)

> Currentlly, only these two models are implemented for learning purposes, but can be extended to include more complex models like computer vision, time series, etc.

---

### 🧭 Repo Structure (High-Level)

This repository is organized to help you navigate through different MLOps components and projects easily. Here's a high-level overview of the structure:

```markdown
mlops-learn-by-building/
│
├── structured_model  Structured ML with full MLOps stack
├── text_model/ ➡️ BERT/NLP-based MLOps pipeline
├── shared/ ➡️ Common utils: logging, data loaders
├── config/ ➡️ YAML-based configuration
├── data/ ➡️ Version-controlled datasets via DVC
├── models/ ➡️ Trained models, logs, metadata
├── monitoring/ ➡️ Drift detection and alerting tools
├── docs/ ➡️ Tutorials and guides for each MLOps component
├── .github/workflows/ ➡️  CI/CD pipelines
└── README.md ➡️  You’re here!
```

### 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

---


> ✍️ This document was partially authored with the assistance of Generative AI tools to improve readability and structure.

> 📝  This repository is a **work in progress**. New tutorials and components will be added over time, so check back often!
