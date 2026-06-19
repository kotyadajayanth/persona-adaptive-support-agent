def should_escalate(query, score):

    query = query.lower()

    if score < 0.5:
        return True

    if "billing" in query:
        return True

    if "refund" in query:
        return True

    if "legal" in query:
        return True

    return False
def generate_handoff(persona, query, sources):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": sources,
        "recommendation": "Human review required"
    }