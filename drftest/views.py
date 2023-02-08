from django.forms import model_to_dict

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Person
from .serializers import PersonSerializer


""" Реализация Viewsets and ModelViewSet"""

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer




# class PersonAPIList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#
# class PersonAPIUpdate(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
# class PersonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer





# class PersonAPIView(APIView):
#     def get(self, request):
#         p = Person.objects.all()
#         return Response({'posts': PersonSerializer(p, many=True).data})
#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error":"Method PUT not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#         serializer = PersonSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Objects does not exists"})
#         return Response({"post": "delete post " + str(pk)})


# class PersonAPIView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
