# 🔐 IAM Policy Visualizer & Misconfiguration Detector

A lightweight web app to analyze AWS IAM policies, detect misconfigurations (like wildcard actions and privilege escalation risks), and visualize permission risks — all without needing actual AWS credentials.

Built using **Python**, **Boto3**, and **Streamlit**.

---

## 🚀 Features

- Paste IAM policy JSON and analyze instantly
- Detects over-permissive policies
- Flags privilege escalation risks
- Highlights wildcard `*` in actions or resources
- Suggests IAM best practices (least privilege)
- No AWS credentials needed — fully offline analysis
- Simple Streamlit UI for quick use



## Sample Input

Paste into the app:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*", "iam:PassRole", "iam:CreateUser"],
      "Resource": "*"
    }
  ]
}



## Clone the repo:
git clone https://github.com/Mohammadakhil/iam-policy-visualizer.git
cd iam-policy-visualizer


## Create Virtual Environment if you not(optional)

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Run the App
streamlit run app.py
