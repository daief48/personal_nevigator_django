from django.shortcuts import HttpResponse
def navigation(request):
    s = '''<h2> Navigation Bar </h2>
    <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django with Harry Bhai</a><br>
    <a href="https://www.facebook.com/">Facebook </a> <br>
    <a href="https://www.daraz.com.bd/">Daraz </a> <br>
    <a href="https://www.prothomalo.com/"> News Paper</a> <br>
    <a href="https://www.google.com/">Google </a> <br>
    '''
    return HttpResponse(s)