import os

import streamlit as st
from dotenv import load_dotenv

from agents.supervisor import Supervisor
from genai_client import GenAIClient
from graph.neo4j_client import Neo4jClient


load_dotenv()


def ask_question(question: str) -> str:
    supervisor = Supervisor()
    genai_client = GenAIClient()

    route = supervisor.planner.route(question)
    if route == "rag":
        answer = supervisor.rag_agent.answer(question)
    else:
        answer = supervisor.graph_agent.answer(question)

    return genai_client.generate(question, answer)


def main() -> None:
    st.title("Salesforce Metadata Agent POC")
    st.caption("Ask about Salesforce metadata relationships or documentation.")

    with st.sidebar:
        st.write("Status")
        neo4j_client = Neo4jClient()
        if neo4j_client.is_configured():
            st.success("Neo4j configured")
        else:
            st.warning("Using sample fallback metadata")

    question = st.text_input("Your question", placeholder="How is Opportunity related to Account and Case?")

    if st.button("Ask") and question:
        with st.spinner("Thinking..."):
            answer = ask_question(question)
        st.markdown("### Answer")
        st.write(answer)


if __name__ == "__main__":
    main()
