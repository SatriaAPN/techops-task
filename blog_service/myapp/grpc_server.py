import grpc
import logging
from concurrent import futures
from proto import blog_service_pb2_grpc
from collections import namedtuple
from .grpc_handler import createBlogHandler, getBlogDetailHandler

logger = logging.getLogger('myapp')

class BlogServiceServicer(blog_service_pb2_grpc.BlogServiceServicer):
    def CreateBlog(self, request, context):
        logger.info('CreateBlog: ', request)

        return createBlogHandler(request)

    def GetBlogDetail(self, request, context):
        logger.info('GetBlogDetail: %s', request)

        return getBlogDetailHandler(request)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blog_service_pb2_grpc.add_BlogServiceServicer_to_server(BlogServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()
