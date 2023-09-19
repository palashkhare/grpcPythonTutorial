from pb.recommendations_pb2 import BookCategory, RecommendationRequest
from main import RecommendationsService

def test_recommendations():
    service = RecommendationsService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=1
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 1