from rest_framework.views import APIView
from .models import Question
from rest_framework.response import Response
from .serializers import QuestionSerializer
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token





class AddQuestionApi(APIView):

    # permission_classes = [permissions.IsAdminUser]

    def post(self,request):

       new_question =  QuestionSerializer(data = request.data)

       if new_question.is_valid():
           new_question.save()
           return Response(new_question.data)


class ViewApiQuestionList(APIView):

    def get(self,request):

        questions = Question.objects.all()
        all_questions = QuestionSerializer(questions,many=True)

        return   Response(all_questions.data)





class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })