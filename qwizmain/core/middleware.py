class CopySesion:

    def __init__(self,response):
        self.response = response

    def __call__(self,request):
        response = self.response(request)
        response['X-MyCustomHeader'] = 'Hello World'
        response['Authorization'] = 'Token  bdc3d5335239c3576f6629a77e3495cea6c33974'
        print(response.items())


        return response