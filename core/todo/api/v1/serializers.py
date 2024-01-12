from rest_framework import serializers
from todo.models import Task, Status
from accounts.models import Profile, User


class Statusserializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]


class Usersserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class Taskserializers(serializers.ModelSerializer):
    absolute_urls = serializers.SerializerMethodField()
    status = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Status.objects.all()
    )
    snippet = serializers.ReadOnlyField(source="get_snippet")

    class Meta:
        model = Task
        fields = [
            "id",
            "author",
            "title",
            "description",
            "snippet",
            "absolute_urls",
            "created_date",
            "status",
        ]
        read_only_fields = ["author"]

    def get_absolute_urls(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("absolute_urls", None)
            rep.pop("snippet", None)
        else:
            rep.pop("description", None)
        rep["status"] = Statusserializers(
            instance.status, context={"request": request}
        ).data
        return rep
