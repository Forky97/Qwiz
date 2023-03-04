from rest_framework import serializers
from .models import Question,CustomUser




class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = '__all__'



class CumstomUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = '__all__'