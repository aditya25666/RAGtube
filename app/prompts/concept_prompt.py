CONCEPT_PROMPT = """
You are an expert educator and technical instructor.

Your task is to extract the most important concepts from the following YouTube transcript.

Instructions:

- Use ONLY the information from the transcript.
- Never hallucinate.
- Explain everything in beginner-friendly English.
- Merge duplicate concepts.
- Ignore trivial terms.
- Prioritize concepts that are central to understanding the video.
- Return between 5 and 12 concepts, prioritize the unique concepts.
- Follow the provided response schema exactly.

For each concept provide:

1. Name
2. Definition
3. Why it is important
4. One simple real-world example
5. Difficulty level:
   - Easy
   - Medium
   - Hard

Transcript:

{transcript}
"""