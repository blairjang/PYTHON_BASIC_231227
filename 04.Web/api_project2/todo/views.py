# from django.shortcuts import render # 페이지 구성안할거니 render 필요없음
from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response # 기본응답  
from rest_framework.views import APIView
from todo.models import Todo
from todo.serializers import TodoSimpleSerializers, TodoDetailSerializer, TodoCreateSerializer
from rest_framework.generics import get_object_or_404 
from rest_framework.decorators import api_view


# 강사님 코드
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = False)
        serializer = TodoSimpleSerializers(todos, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id = id) # todo 안에서 id 가 일치하는것을 찾고  
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def put(self, request, id): # 수정 기능 
       todo = get_object_or_404(Todo, id = id)
       serializer = TodoCreateSerializer(todo, data= request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete = True) # or 무조건 전체임 그러나 filter 은 조건식임
        serializer = TodoSimpleSerializers(dones, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
    def get(self, request, id):
        done = get_object_or_404(Todo, id = id)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(status = status.HTTP_200_OK)