from datetime import datetime, timezone
from django.http.response import HttpResponse
from rest_framework import status, serializers
from .models import SubCategory
from .serializers import SubCategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET', 'POST'])
def create_and_list_sub_category(request):
    """Have ICT able to create subcategory"""
    if request.method == 'GET':
        sub_category = SubCategory.objects.filter(is_deleted=False)
        serializer = SubCategorySerializer(sub_category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])
def edit_and_delete_sub_category(request, pk):
    """
    Have ICT able to update manipulate
    (Update, Delete) a specific Sub Category
    """
    try:
        subcategory = SubCategory.objects.get(
            pk=pk, is_deleted=False)
    except SubCategory.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        updated_by = request.data.get('updated_by')
        if updated_by is None:
            response = {
                "message": "Request was not successfull include updated_by"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['updated_by'] = datetime.now(
                timezone.utc)
            serializer.save()
            response = {
                "message": "Success SubCategory has been updated."
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        
        # subcategory.deleted_on = datetime.now(timezone.utc)
        # subcategory.deleted_by = deleted_by
        subcategory.save()
        response = {
                "message": "SubCategory has been successfuly deleted"
            }
        return Response(response, status=status.HTTP_200_OK)