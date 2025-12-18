# Dialogflow Setup & Quick Guide

This guide covers creating a simple Dialogflow ES agent and adding FAQ intents based on `sample_faq.csv`.

1. Create a Google Cloud Project and enable Dialogflow API
   - Go to https://console.cloud.google.com/ and create/select a project.
   - Enable the Dialogflow API and billing if required.

2. Open Dialogflow Console
   - Visit https://dialogflow.cloud.google.com/ and create an agent (select the GCP project).

3. Create Intents (manual method)
   - In Dialogflow Console, go to "Intents" → "Create Intent".
   - Use the `intent` column from `sample_faq.csv` as the Intent name.
   - For each intent, add the sample questions as "Training phrases" (the `question` column).
   - Add the `answer` text as the "Responses" content.

4. Test in the Dialogflow Console
   - Use the right-hand chat panel to type messages like "Where is my order?" and confirm the correct intent/response.

5. Export / Import (optional)
   - Dialogflow allows you to export the entire agent as a ZIP. For bulk imports, you can prepare intent JSONs and upload.

6. Integrations
   - Dialogflow provides built-in Integrations (e.g., Web Demo, Telegram, Facebook Messenger). Use the Integrations page to enable a direct channel.
   - For Telegram, follow Dialogflow's Telegram integration steps or use a webhook to forward messages.

7. Fallback and small-talk
   - Create a `Default Fallback Intent` for unknown queries and add helpful suggestions.
   - Add a `greet` intent and basic small-talk responses (hello, thanks).

Notes
   - For a production bot you'll want to add contexts, slot-filling, and entity extraction for order IDs, dates, etc.
   - Keep training phrases varied to improve matching.
