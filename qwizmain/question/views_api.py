from rest_framework.views import APIView
from .models import Question
from rest_framework.response import Response
from .serializers import QuestionSerializer



class AddQuestionApi(APIView):

    def post(self,request):

       new_question =  QuestionSerializer(data = request.data)

       if new_question.is_valid():
           new_question.save()
           return Response(new_question.data)



