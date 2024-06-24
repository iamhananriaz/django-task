# from django.http import HttpResponse

# class ExceptionMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         return self.get_response(request)

#         user_agent = request.META.get('HTTP_USER_AGENT')
        
#         print('###')
#         print(user_agent)
#         print('##')

#     def process_exception(self, request, exception): 
#         print("----working--------")
#         return HttpResponse("in exception")
