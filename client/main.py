import grpc
import os

from pb.recommendations_pb2_grpc import RecommendationsStub
from pb.recommendations_pb2 import BookCategory, RecommendationRequest


PORT = os.environ.get("GRPC_PORT", "50050")
HOST = os.environ.get("GRPC_HOST", "localhost")

channel = grpc.insecure_channel(f"{HOST}:{str(PORT)}")
client = RecommendationsStub(channel=channel)

# Prepare request (Request serializer)
recommendation_request = RecommendationRequest(
    user_id = 1,
    category = BookCategory.MYSTERY,
    max_results = 4,
)

try:
    result = client.Recommend(
        recommendation_request
    )
    print(result.recommendations[0])
except Exception as e:
    print(
        "Request Failed : ",
        str(e)
    )