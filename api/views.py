from django.shortcuts import render

from api.models import Category, Game
from api.serializers import CategorySerializer, GameSerializer

from rest_framework.response import Response
from rest_framework.views import status

from rest_framework.decorators import api_view
from rest_framework.views import APIView

class CategoryListView(APIView):
    def get(self, request):
        try:
            serializer = CategorySerializer(Category.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "There is an error reading categories from database"}, status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request):
        Category.objects.create(
            name = request.data.get('name')
        )
        return Response({"message": "Category successfully created."}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def category_detailed(request, id):
    try:
        serializer = CategorySerializer(Category.objects.get(id=id))
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "There is an error reading category from database"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['PUT', 'DELETE'])
def category_admin_actions(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response({"error": "There is an error reading category from database"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response({"message": "Category succesfully updated."}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        category.delete()
        return Response({"message": "Category succesfully deleted."}, status=status.HTTP_200_OK)


class GamesView(APIView):
    def get(self, request):
        try:
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Error getting games"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            category = Category.objects.get(name=request.data.get('cat'))
        except:
            return Response({"error": "There is an error reading category from database"}, status=status.HTTP_404_NOT_FOUND)

        Game.objects.create(
            name = request.data.get('name'),
            description = request.data.get('description'),
            image = request.data.get('image'),
            category = category,
            price = request.data.get('price'),
            screenshots = request.data.get('screenshots'),
            text = request.data.get('text')
        )

        return Response({"message": "here's data about games. LOL"}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def game_details(request, id):
    try:
        game = Game.objects.get(id=id)
    except:
        return Response({"error": "Error getting games"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(GameSerializer(game).data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            category = Category.objects.get(id=request.data.get('id'))
        except:
            return Response({"error": "There is an error reading category from database"}, status=status.HTTP_404_NOT_FOUND)
        game.name = request.data.get('name')
        game.description = request.data.get('name')
        game.image = request.data.get('name')
        game.category = category
        game.price = request.data.get('name')
        game.screenshots = request.data.get('name')
        game.text = request.data.get('name')
        game.save()
        return Response({"message": "Game update"}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        game.delete()
        return Response({"message": "game delete"}, status=status.HTTP_200_OK)


