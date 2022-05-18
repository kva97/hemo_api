from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HemoTestSerializer
from .models import HemoTest
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/finished_tests/',
            'method': 'GET',
            'body': None,
            'desc': 'Returns full story of tests'
        },
        {
            'Endpoint': '/finished_tests/id',
            'method': 'GET',
            'body': None,
            'desc': 'Returns a single test'
        },
        {
            'Endpoint': '/create_new_hemotest/',
            'method': 'POST',
            'body': {'body': ""},
            'desc': 'Returns a create test'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getHemoTests(request):
    tests = HemoTest.objects.all()
    serializer = HemoTestSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSpecificHemoTest(request, pk):
    test = HemoTest.objects.get(id=pk)
    serializer = HemoTestSerializer(test, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNewHemoTest(request):
    data = request.data

    hemoTest = HemoTest.objects.create(
        body=data['body']
    )

    serializer = HemoTestSerializer(hemoTest, many=False)
    return Response(serializer.data)


#Потребуется для обновления данных пользователя
@api_view(['POST'])
def updateUserData(request, pk):
    data = request.data

    hemoTest = HemoTest.objects.get(id=pk)

    serializer = HemoTestSerializer(hemoTest, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)