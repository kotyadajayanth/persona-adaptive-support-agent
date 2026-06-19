def detect_persona(message):

    message = message.lower()

    technical_words = [
        "api",
        "error",
        "log",
        "authentication",
        "configuration",
        "endpoint",
        "token"
    ]

    frustrated_words = [
        "frustrated",
        "angry",
        "urgent",
        "nothing works",
        "failed",
        "issue",
        "problem",
        "not working",
        "password"
    ]

    executive_words = [
        "business",
        "impact",
        "operations",
        "revenue",
        "timeline",
        "executive"
    ]

    for word in technical_words:
        if word in message:
            return "Technical Expert"

    for word in frustrated_words:
        if word in message:
            return "Frustrated User"

    for word in executive_words:
        if word in message:
            return "Business Executive"

    return "Frustrated User"