class Prescriber:
    """Rule-based or AI-assisted drug recommendation system."""

    def recommend(self, symptoms: str) -> str:
        symptoms = symptoms.lower()

        if "headache" in symptoms:
            return "Paracetamol 500mg every 6 hours as needed for pain."
        elif "fever" in symptoms:
            return "Ibuprofen 400mg or Acetaminophen 500mg to reduce fever."
        elif "cough" in symptoms:
            return "Cough syrup containing dextromethorphan or honey lemon tea."
        elif "sore throat" in symptoms:
            return "Warm saline gargle and lozenges; if bacterial, amoxicillin 500mg."
        elif "stomach" in symptoms or "nausea" in symptoms:
            return "Oral rehydration salts and antacid if necessary."
        else:
            return "No clear match found. Please consult a doctor for further evaluation."
