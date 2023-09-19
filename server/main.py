from concurrent import futures
import os
import grpc
import random

from pb.recommendations_pb2_grpc import RecommendationsServicer, add_RecommendationsServicer_to_server
from pb.recommendations_pb2 import RecommendationResponse, SingleOutput

from books_db import BOOKS_BY_CATEGORY


PORT = os.environ.get("GRPC_PORT", "50050")

class RecommendationsService(RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in BOOKS_BY_CATEGORY:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        books_for_category = BOOKS_BY_CATEGORY[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )

        return RecommendationResponse(recommendations=books_to_recommend)

    def Dummy(self, request, context):
        return SingleOutput(
            response="Test response success!"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RecommendationsServicer_to_server(
        RecommendationsService(), server
    )
    server.add_insecure_port(f"[::]:{str(PORT)}")

    print("Starting Server...")
    try:
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Gracefully shutting down...")


if __name__ == "__main__":
    serve()