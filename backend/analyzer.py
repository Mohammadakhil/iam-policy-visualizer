import json
from policyuniverse.policy import Policy

def analyze_policy(policy_str):
    findings = []
    try:
        policy = Policy(policy_str)
        if policy.is_allow_all_actions():
            findings.append("❗ Policy allows all actions: '*'")
        if policy.is_allow_all_resources():
            findings.append("❗ Policy allows all resources: '*'")
        if policy.missing_resource_constraints():
            findings.append("⚠️ No resource constraints found in policy")

        if not findings:
            findings.append("✅ No obvious misconfigurations found.")
    except Exception as e:
        findings.append(f"Error parsing policy: {str(e)}")
    return findings
