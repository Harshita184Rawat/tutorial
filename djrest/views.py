from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from djrest.models import Djrest
from django.http import Http404
from rest_framework.views import APIView
from djrest.serializers import DjrestSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from djrest.serializers import UserSerializer
from rest_framework import permissions
from djrest.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'djrest': reverse('djrest-list', request=request, format=format)
    })
    
class DjrestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Djrest.objects.all()
    serializer_class = DjrestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
 
 

'''
class DjrestList(APIView):
    """
    List all djrests, or create a new djrest.
    """
    def get(self, request, format=None):
        djrest = Djrest.objects.all()
        serializer = DjrestSerializer(djrest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DjrestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DjrestDetail(APIView):
    """
    Retrieve, update or delete a djrest instance.
    """
    def get_object(self, pk):
        try:
            return Djrest.objects.get(pk=pk)
        except Djrest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        djrest = self.get_object(pk)
        serializer = DjrestSerializer(djrest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        djrest = self.get_object(pk)
        serializer = DjrestSerializer(djrest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        djrest = self.get_object(pk)
        djrest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


'''@api_view(['GET', 'POST'])
def djrest_list(request):
    """
    List all code djrests, or create a new djrest.
    """
    if request.method == 'GET':
        djrest = Djrest.objects.all()
        serializer = DjrestSerializer(djrest, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DjrestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def djrest_detail(request, pk):
    """
    Retrieve, update or delete a code djrest.
    """
    try:
        serializer = Djrest.objects.get(pk=pk)
    except Djrest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DjrestSerializer(djrest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DjrestSerializer(djrest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        djrest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''
    
'''@csrf_exempt
def djrest_list(request):
    """
    List all code djrest, or create a new djrest.
    """
    if request.method == 'GET':
        djrest = djrest.objects.all()
        serializer = djrestSerializer(djrest, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def djrest_detail(request, pk):
    """
    Retrieve, update or delete a code djrest.
    """
    try:
        djrest = djrest.objects.get(pk=pk)
    except djrest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(djrest)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = djrestSerializer(djrest, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        djrest.delete()
        return HttpResponse(status=204)'''
