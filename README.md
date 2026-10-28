# Email Spam Detection

A small Python project that classifies email text as **spam** or **ham** (legitimate email). It cleans email text with spaCy, converts text into bag-of-words features, trains a Multinomial Naive Bayes classifier, and exposes predictions through a FastAPI endpoint.

## Features

- Text cleaning with spaCy lemmatization and stop-word removal
- CountVectorizer features using unigrams and bigrams
- Multinomial Naive Bayes classifier
- Interactive command-line prediction
- FastAPI prediction endpoint (`POST /predict`)
- Spam messages received by the API are appended to a local quarantine CSV

## Repository layout

```text
email-spam-detection/
├── data/
│   ├── raw/                   # Source dataset (email_text,label)
│   ├── processed/             # Generated cleaned dataset
│   └── quarantine/            # Runtime spam log; do not commit real email content
├── models/                    # Serialized vectorizer and trained classifier
├── src/
│   ├── api/                   # FastAPI app
│   ├── data/                  # Loading and text preprocessing
│   ├── features/              # Vectorizer preparation
│   ├── models/                # Training, evaluation, prediction
│   └── quarantine/            # Quarantine CSV helper
├── main.py                    # Runs dataset preprocessing
├── requirements.txt
└── README.md
```

The local `.venv/` should not be uploaded. It is recreated on each machine from `requirements.txt`.

## Requirements

- Python 3.10 or later
- The spaCy English model `en_core_web_sm`

## Setup

Run these commands from the repository root.

### Windows PowerShell

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Prepare data and models

The repository includes the current dataset, processed data, and trained model files. To rebuild them from the raw dataset, run:

```bash
python main.py
python -m src.features.vectorizer
python -m src.models.train
```

To print the classification report and confusion matrix:

```bash
python -m src.models.evaluate
```

## Predict from the command line

```bash
python -m src.models.predict
```

Enter an email when prompted. Stop the program with `Ctrl+C`.

## Run the API

```bash
uvicorn src.api.app:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API page. Example request:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Congratulations, claim your prize now!"}'
```

Example response:

```json
{"label":"spam"}
```

When the prediction is `spam`, the API stores the submitted text in `data/quarantine/quarantine.csv`. Avoid sending private or sensitive email content to this local demo API. The quarantine file is excluded from Git by the included `.gitignore`.

## Dataset format

The raw CSV is expected at `data/raw/email_spam_dataset.csv` with these columns:

| Column | Description |
| --- | --- |
| `email_text` | Original email text |
| `label` | `spam` or `ham` |

If you replace the dataset, make sure you have the right to redistribute it and document its original source and license here.

## Notes

- The API and scripts use paths relative to the repository root; run them from that directory.
- Model files are Python pickle/joblib artifacts. Only load artifacts you trust, and retrain them if you change the data or preprocessing.
- This is a learning/demo project. Evaluate it on representative data before relying on its predictions.

## License

No license has been added yet. Choose a license before making the repository public if you want to grant others permission to reuse the code.
