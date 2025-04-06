🌱 AgroSAP: AI-Powered Soil Remediation Platform

AgroSAP is a scrappy MVP for an AI-powered soil remediation platform that uses superabsorbent polymers (SAPs) to capture heavy metals in contaminated soil. This project originated from the Little Bang UC Davis Pitch Competition, where it won $1,000 in seed funding. AgroSAP aims to empower farmers with actionable, data-driven insights to optimize soil health and ensure sustainable agricultural practices.


## Project Features

- Data Modeling:
  Python-based absorption model to predict SAP efficiency based on metal concentration levels in the soil.

- Simulation Engine:
  Remediation simulation calculates impact over time and tracks improvements in soil condition.

- Supabase Integration:
  Cloud backend using Supabase to store and manage soil sample data in real time.

- RESTful API:
  Flask-based API (`/simulate`) to integrate with external services or future mobile/web clients.

- Interactive Dashboard:
  Built with Streamlit to upload CSVs, run models, visualize contamination levels, and show remediation predictions.

- HashMap Data Structure:
  Fast lookup of soil samples by ID to support efficient querying and expansion into field-level analysis.

- C++ Backend Stub:
  Simple absorption calculation function written in C++ for future performance-critical simulations.

---

## Tech Stack
- Python 3.10 – main logic and data pipeline
- Streamlit – MVP dashboard UI
- Flask – RESTful API
- Supabase – cloud storage and backend
- C++ – backend computation prototype
- pandas / scikit-learn / matplotlib – data analysis and visualization


## File Structure
```
project_root/
├── README.md
├── requirements.txt
├── main.py
├── supabase_config.py
├── supabase_helpers.py
├── api.py
├── dashboard.py
├── cpp/
│   └── remediation.cpp
├── src/
│   ├── ingest.py
│   ├── model.py
│   ├── simulate.py
│   ├── visualize.py
│   └── data_structures.py
├── data/
│   └── soil_sample.csv
└── .env (DO NOT COMMIT!)
```


## How to Run
```bash
# Clone the repo
$ git clone https://github.com/yourusername/agrosap-mvp.git
$ cd agrosap-mvp

# Set up virtual environment and install dependencies
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# Add your Supabase credentials to .env (not committed)
SUPABASE_URL=your_url_here
SUPABASE_KEY=your_key_here

# Run main pipeline
$ python main.py

# Start dashboard
$ streamlit run dashboard.py

# Start API
$ python api.py
```



## Use Cases & Value
- Farmers: Identify toxic soil zones and apply the right amount of SAP to maximize yield
- Sustainability Researchers: Simulate long-term impact of polymer-based soil remediation
- AgTech Startups: Integrate with field sensors or drone data in future iterations

---

## Recognition
- Winner of Little Bang UC Davis Pitch Competition ($1,000)
- Validated by sustainability experts and early testers

---

## Security Notice
Do NOT commit your `.env` file containing your Supabase credentials. Always use `.gitignore` to exclude secrets.

---

## Contact
Have feedback or want to collaborate?
Created by Pranavi Khanna – Software Engineer & Product Manager
[LinkedIn](https://www.linkedin.com/in/pranavikhanna) | [Email](mailto:your-email@ucdavis.edu)


Built with 💡 at UC Davis.
