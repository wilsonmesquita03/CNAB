from rest_framework.views import APIView, Response, status
from rest_framework.generics import ListAPIView
from .parsers import FileUploadParser
import ipdb
from .utils import get_type, get_nature, get_date, get_value, get_hour
from .serializers import CnabSerializer
from stores.models import Store
from .models import Cnab
from rest_framework.exceptions import ValidationError


# Create your views here.
class CreateCnabView(ListAPIView, APIView):
    parser_classes = [FileUploadParser]
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer
    
    def post(self, request, filename="cnab", format=None):
        uploaded_file = request.FILES['file']
        str_text = ''
        for line in uploaded_file:
            str_text = str_text + line.decode()

        cnabs = str_text.split("\r\n")[1:]

        for cnab in cnabs:
            cnab_dict = {
                "type": get_type(cnab[0]),
                "nature": get_nature(cnab[0]),
                "date": get_date(cnab[1:9]),
                "value": get_value(cnab[9:19]),
                "cpf": cnab[19:30],
                "card": cnab[30:42],
                "hour": get_hour(cnab[42:48]),
                "store_owner_name": cnab[48:62].strip(),
                "store_name": cnab[62:81].strip()
            }

            store_obj, created = Store.objects.get_or_create(name=cnab_dict['store_name'], owner_name = cnab_dict['store_owner_name'])

            cnab_already_exists = Cnab.objects.filter(store=store_obj, type=cnab_dict["type"], hour=cnab_dict["hour"], date=cnab_dict["date"]).exists()

            serializer = CnabSerializer(data=cnab_dict)

            serializer.is_valid(raise_exception=True)

            if cnab_already_exists:
                raise ValidationError(
                    {
                        "detail": "this transaction has already been saved before",
                        "transation": serializer.validated_data
                    }
                )

            serializer.save(store=store_obj)

        return Response(status=201)