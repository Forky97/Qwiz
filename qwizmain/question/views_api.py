from rest_framework.views import APIView
from .models import Question
from rest_framework.response import Response
from .serializers import QuestionSerializer
from rest_framework import permissions



class AddQuestionApi(APIView):

    permission_classes = [permissions.IsAdminUser]

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



