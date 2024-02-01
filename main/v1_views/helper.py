from rest_framework.response import Response



class No_method():
    
    def get(self, request):
        return Response({
            'error':'Bunaqa method ishlamaydi'
        })
    
    def post(self, request):
        return Response({
            'error':'Bunaqa method ishlamaydi'
        })
    
    def delete(self, request):
        return Response({
            'error':'Bunaqa method ishlamaydi'
        })
    
    def put(self, request):
        return Response({
            'error':'Bunaqa method ishlamaydi'
        })
    
    def patch(self, request):
        return Response({
            'error':'Bunaqa method ishlamaydi'
        })
    



    