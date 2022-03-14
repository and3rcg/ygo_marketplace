from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import User

class LoginView(APIView):
    def post(self, request):
        user = request['username']
        password = request['password']
        
        try:
            user = User.objects.get(username=user)
            if user.check_password(password):
                # TODO return a token
                return Response({'message':'Login successful!'})
            else:
                return Response({'message':'Incorrect user or password.'})
        
        except User.DoesNotExist:
            return Response({'message':'Incorrect user or password.'})
