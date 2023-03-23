from django.shortcuts import render
import pyfiglet


def text_to_ascii(request):
    fonts = pyfiglet.FigletFont.getFonts()
    text = request.GET.get('text', '')
    font = request.GET.get('font', 'slant')

    result = pyfiglet.figlet_format(text, font=font)
    context = {
        'fonts': sorted(fonts),
        'result': result
    }
    return render(request, 'textart.html', context)
