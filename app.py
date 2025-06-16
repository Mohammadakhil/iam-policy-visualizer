import streamlit as st
import json

st.set_page_config(page_title="IAM Policy Visualizer", layout="wide")
st.title("🔐 IAM Policy Visualizer & Misconfiguration Detector")

st.markdown("""
Paste your **IAM Policy JSON** below. This tool checks for:
- 🔓 Wildcard (`*`) actions and resources
- 🔥 Dangerous IAM actions (e.g., `iam:CreateUser`, `iam:PassRole`)
- ❌ Overly permissive configurations
""")

# Sample risky actions
dangerous_actions = {
    "iam:CreateUser", "iam:PutUserPolicy", "iam:AttachUserPolicy",
    "iam:CreateAccessKey", "iam:PassRole", "iam:UpdateAssumeRolePolicy",
    "iam:CreatePolicyVersion", "iam:AttachRolePolicy"
}

# Input
policy_input = st.text_area("📋 Paste IAM Policy JSON here", height=300)

# Analyzer
def analyze_iam_policy(policy_text):
    results = []

    try:
        policy = json.loads(policy_text)

        statements = policy.get("Statement", [])
        if not isinstance(statements, list):
            statements = [statements]

        wildcard_actions = set()
        wildcard_resources = set()
        found_dangerous = set()

        for stmt in statements:
            actions = stmt.get("Action", [])
            resources = stmt.get("Resource", [])

            # Normalize to list
            if isinstance(actions, str):
                actions = [actions]
            if isinstance(resources, str):
                resources = [resources]

            # Check for wildcards and dangerous actions
            for action in actions:
                if "*" in action:
                    wildcard_actions.add(action)
                if action.lower() in [d.lower() for d in dangerous_actions]:
                    found_dangerous.add(action)

            for res in resources:
                if res == "*":
                    wildcard_resources.add(res)

        if wildcard_actions:
            results.append(f"⚠️ Wildcard actions found: {', '.join(sorted(wildcard_actions))}")

        if wildcard_resources:
            results.append(f"⚠️ Wildcard resource access: {', '.join(wildcard_resources)}")

        if found_dangerous:
            results.append(f"🚨 Dangerous IAM actions detected: {', '.join(sorted(found_dangerous))}")

        if not results:
            results.append("✅ No major misconfigurations detected.")

    except Exception as e:
        results.append(f"❌ Error analyzing policy: {str(e)}")

    return results

# Button
if st.button("Analyze Policy"):
    results = analyze_iam_policy(policy_input)
    st.subheader("🔍 Analysis Results")
    for line in results:
        st.write(line)
