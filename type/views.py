from django.shortcuts import render
import os
import keyboard

def text_display(request):
    """while True:
        if keyboard.read_key() == '3':
            return render(request,'type/main.html', {'key_press':'3 was pressed.'})
        else:
            return render(request,'type/main.html', {'key_press': 'No/Wrong key pressed.'})"""   
    char_no = request.session.get('char_no', -1) + 1  
    request.session['char_no'] = char_no
    f = open(os.path.dirname(os.path.realpath(__file__)) + '\\text1.txt', "r+")
    file_contents = f.read()
    if char_no >= len(file_contents):
        return render(request,'type/main.html',{"key_press":"Test is over"})
    for line in file_contents:
        for ch in line:
            if keyboard.read_key() == file_contents[char_no]:
                ctx = {'text': file_contents, 'key_press':'You pressed the right key.'}
                f.close()
                return render(request, 'type/main.html', ctx)
            else:
                ctx = {'text': file_contents, 'key_press':'You pressed the wrong key.'}
                return render(request, 'type/main.html', ctx)

