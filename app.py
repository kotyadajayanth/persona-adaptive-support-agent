import streamlit as st

from src.classifier import detect_persona
from src.rag import get_context
from src.rag import load_documents
from src.generator import generate_response
from src.escalation import should_escalate
from src.escalation import generate_handoff

load_documents()

st.title("Persona Adaptive Customer Support Agent")

query = st.text_input("Enter your question")

if st.button("Submit"):

    persona = detect_persona(query)

    context, sources, score = get_context(query)

    escalation = should_escalate(query, score)

    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("Retrieved Sources")
    st.write(sources)

    if escalation:

        handoff = generate_handoff(
            persona,
            query,
            sources
        )

        st.subheader("Escalation Status")
        st.error("Escalated to Human Agent")

        st.subheader("Handoff Summary")
        st.json(handoff)

    else:

        response = generate_response(
            query,
            persona,
            context
        )

        st.subheader("Response")
        st.write(response)

        st.subheader("Escalation Status")
        st.success("No Escalation Required")