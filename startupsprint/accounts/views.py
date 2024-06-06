from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAdminUser  # Import the custom IsAdminUser permission
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    

    def get(self, request):
        # Admin can see all customer information
        customers = User.objects.filter(role='customer')
        serializer = UserSerializer(customers, many=True)
        return Response(serializer.data)
        

       

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, request):
        user = get_object_or_404(User, pk=pk)
        if not request.user.is_staff and user != request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return user

    def get(self, request, pk):
        user = self.get_object(pk, request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk, request)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = self.get_object(pk, request)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk, request)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
