def generate_response(question, docs):

    context = "\n".join([doc.page_content for doc in docs])

    response = f"""
Based on the banking knowledge base:

{context[:700]}
"""

    return response