from app.services.vector_service import VectorService

vector_service = VectorService()

retriever = vector_service.get_retriever()

docs = retriever.invoke("What is a retriever?")

print(f"Retrieved {len(docs)} documents\n")

for i, doc in enumerate(docs):
    print("=" * 80)
    print(f"Document {i+1}")
    print(doc.metadata)
    print()
    print(doc.page_content[:500])