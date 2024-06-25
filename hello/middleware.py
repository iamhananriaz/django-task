class testmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Before view')

        response = self.get_response(request)
        
        print('After view')

        return response
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     response = self.get_response(request)
    #     response['X-Custom-Header'] = 'My Custom Value'
    #     return response