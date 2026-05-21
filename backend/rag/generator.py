def generate_response(context, question):

    if not context:
        return "No relevant information found."

    sentences = context.split(".")

    filtered_sentences = []

    for sentence in sentences:

        sentence = sentence.strip()

        if (
            len(sentence) > 30
            and "AI Banking Knowledge Base Dataset" not in sentence
            and "synthetic banking knowledge" not in sentence
            and sentence not in filtered_sentences
        ):
            filtered_sentences.append(sentence)

    final_answer = ". ".join(filtered_sentences[:4])

    return final_answer + "."