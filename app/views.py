from rest_framework.decorators import api_view

from app.response import SuccessResponse

@api_view(['GET'])
def home():
    pass

@api_view(['POST'])
def generate_report():
    pass

@api_view(['GET'])
def report():
    pass