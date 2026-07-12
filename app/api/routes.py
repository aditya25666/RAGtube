from fastapi import APIRouter
from pydantic import BaseModel

from app.services.index_service import IndexService

from app.services.summary_service import SummaryService

from app.services.concept_service import ConceptService

from app.services.chat_service import ChatService

router = APIRouter()


class VideoRequest(BaseModel):
    url: str


@router.post("/process-video")
def process_video(request: VideoRequest):

    index_service = IndexService()

    return index_service.process_video(request.url)


class SummaryRequest(BaseModel):
    video_id: str

@router.post("/summary")
def generate_summary(request: SummaryRequest):

    summary_service = SummaryService()

    return summary_service.generate_summary(
        request.video_id
    )


class SummaryRequest(BaseModel):
    video_id: str

@router.post("/concepts")
def generate_concepts(request: SummaryRequest):

    concept_service = ConceptService()

    return concept_service.generate_concepts(
        request.video_id
    )


class ChatRequest(BaseModel):
    video_id: str
    question: str

@router.post("/chat")
def chat(request: ChatRequest):

    chat_service = ChatService()

    return chat_service.ask(
        video_id=request.video_id,
        question=request.question,
    )