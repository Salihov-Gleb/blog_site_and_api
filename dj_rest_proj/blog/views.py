import random
import string
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.serializers import *
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView


class RandomGenerationView(APIView):
    def post(self, request):
        user_names = ['Victor', 'Elena', 'Ivan', 'UserSuper', 'Bred', 'Doctor']
        if len(User.objects.all()) == 0:
            for i in range(10):
                user_name = random.choice(user_names) + str(random.randint(0, 1000))
                password = str(random.randint(1000000, 99999999999))
                User.objects.create_user(user_name, password=password)
        if len(Category.objects.all()) == 0:
            for i in range(20):
                Category.objects.create(title=f'category{i + 1}')
        title = f"{random.choice(['Title', 'Blog', 'Story', 'Page'])}{random.randint(1, 300)}"
        category = random.choice(Category.objects.all())
        author = random.choice(User.objects.all())
        txt = " ".join(''.join(random.sample(string.ascii_letters, random.randint(3, 6))) for s in range(20))
        try:
            data = BlogNote.objects.create(title=title, author=author, txt=txt)
        except:
            return Response(status=status.HTTP_201_CREATED)
        data.category.add(category)
        return Response(status=status.HTTP_201_CREATED)


class BlogNoteListView(ListAPIView):
    serializer_class = BlogNoteSerializer
    model = BlogNoteSerializer.Meta.model
    queryset = model.objects.all()


class BLogNoteCategoryListView(ListAPIView):
    serializer_class = BlogNoteSerializer
    model = BlogNoteSerializer.Meta.model

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return self.model.objects.filter(category__pk=category_pk)


class BLogNoteAuthorListView(ListAPIView):
    serializer_class = BlogNoteSerializer
    model = BlogNoteSerializer.Meta.model

    def get_queryset(self):
        author_pk = self.kwargs['pk']
        return self.model.objects.filter(author__pk=author_pk)


class BLogNoteRetrieveView(RetrieveAPIView):
    serializer_class = BlogNoteSerializer
    model = BlogNoteSerializer.Meta.model
    queryset = model.objects.all()