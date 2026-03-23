# MedChatAi

MedChat AI is a conversational medical chatbot that analyses patient-reported symptoms alongside biometric data — age, sex, height, and weight — to generate evidence-based drug prescription recommendations.

### Built on a LangChain + Google Gemini reasoning pipeline with a FastAPI backend and Streamlit interface 
It performs multi-step clinical decision-making including differential diagnosis, weight-adjusted dosing, and contraindication checks.

# Why LangChain?
The core problem in MedChatAI isn't just "ask an AI a question" — it's a multi-step reasoning workflow. The system needs to do several things in sequence: extract symptoms from messy free text, run a differential diagnosis, pull in biometric data, calculate a weight-adjusted dose, cross-check contraindications, and finally format a structured prescription. That is a chain of tasks, not a single prompt.
LangChain exists precisely for this. It provides the scaffolding to connect those steps together, pass outputs from one stage as inputs to the next, manage conversation memory across multi-turn patient dialogue, and integrate external tools into the reasoning pipeline. Without LangChain, all that orchestration logic would be written from scratch.

# Why Google Gemini?
Three specific reasons for this project:

### Long context window. 
A patient conversation can be lengthy — symptom history, follow-up questions, medication lists. Gemini's large context window means the model holds the full conversation in memory without truncation, which matters for clinical accuracy.

### Multimodal readiness. 
Future versions of VitalScript AI could accept uploaded lab reports, prescription images, or medical scans. Gemini is natively multimodal, so the architecture doesn't need to be rebuilt to support that.
### Google ecosystem integration. 
The stack already uses google-genai and langchain-google-genai — both are first-party SDKs meaning lower latency, better rate limits, and direct compatibility with Google Cloud infrastructure if the project scales into a production healthcare deployment.

LangChain owns the workflow, Gemini owns the reasoning. That makes the system maintainable, testable, and upgradeable independently at each layer.
