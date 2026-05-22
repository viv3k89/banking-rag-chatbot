def generate_response(question, docs):

    context = "\n".join([doc.page_content for doc in docs])

    responses = f"""
Based on the banking knowledge base:

{context[:700]}
"""

    return responses