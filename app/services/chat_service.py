from app.schemas.chat_schema import CHAT_SCHEMA
from app.services.context_service import ContextService
from app.services.generation_service import GenerationService
from app.services.prompt_service import PromptService
from app.services.retrieval_service import RetrievalService


class ChatService:
    """
    Orchestrates the complete RAG pipeline.
    """

    def __init__(self):

        self.retrieval_service = RetrievalService()
        self.context_service = ContextService()
        self.prompt_service = PromptService()
        self.generation_service = GenerationService()

    def ask(
        self,
        video_id: str,
        question: str,
    ):

        # Step 1 : Retrieve relevant documents
        documents = self.retrieval_service.retrieve(
            video_id=video_id,
            question=question,
        )

        # Step 2 : Build context
        context, sources = self.context_service.build_context(
            documents
        )

        # Step 3 : Build prompt
        prompt = self.prompt_service.build_prompt(
            question=question,
            context=context,
        )

        # Step 4 : Generate answer
        answer = self.generation_service.generate(
            prompt=prompt,
            response_schema=CHAT_SCHEMA,
        )

        # Step 5 : Return final response
        return {
            "video_id": video_id,
            "question": question,
            "answer": answer["answer"],
            "confidence": answer["confidence"],
            "sources": sources,
        }