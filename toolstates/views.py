from datetime import datetime, timezone
from rest_framework import status, serializers
from .models import ItemState
from .serializers import ItemStateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def create_and_list_item_state(request):
    if request.method == 'GET':
        request_object = ItemState.objects.filter(is_deleted=False)
        serializer = ItemStateSerializer(request_object, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemStateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def list_update_delete_item_state_by_id(request, pk):
    try:
        request_object = ItemState.objects.get(pk=pk)
    except ItemState.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            request_object = ItemState.objects.filter(
                is_deleted=False, pk=pk)
            serializer = ItemStateSerializer(
                request_object, many=True)
            return Response(serializer.data)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            raise serializers.ValidationError({"message": message})

    elif request.method == 'PUT':
        serializer = ItemStateSerializer(
            request_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        request_object.is_deleted = True
        request_object.save()
        response = {
                "message": "Request has been successfuly deleted"
            }
        return Response(response, status=status.HTTP_200_OK)