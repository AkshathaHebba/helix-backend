from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from questions.models import Questions
from questions.serializers import QuestionsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def questions_list(request):
    if request.method == 'GET':
        tutorials = Questions.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = QuestionsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        question_serializer = QuestionsSerializer(data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse(question_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Questions.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)