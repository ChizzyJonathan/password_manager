from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def generate_passwords_view(request):
    if request.method == 'POST':
        names = [request.POST.get(f"favourite_word_{i + 1}") for i in range(5)]
        numbers = [request.POST.get(f"favourite_number_{i + 1}") for i in range(2)]
        punctuations = string.punctuation.replace("[", "").replace("]", "").replace("'", "")
        specialchars = {"a": "@", "s": "$", "i": "!", "r": "#", "x": "%", "q": "&", "c": "(", "j": ")", "o": "0", "e": "£", "b": "8", "k": "<", "l": "|"}
        passwords = []
        for i in range(1, 6):
            words = random.sample(names, 2)
            number = random.choice(numbers)
            password = "".join(random.choice([str.upper, str.lower])(c) for c in "".join(words))
            password = "".join([specialchars.get(c, c) for c in password])
            password = f"{password}{number}{random.choice(punctuations)}"
            password = "".join(random.sample(password, len(password)))
            password = password[:12] # limit password length to 12 characters
            passwords.append(password)
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        request.session['passwords'] = passwords
        request.session['key'] = key
        return render(request, 'password_generator/generated_passwords.html', {'key': key, 'passwords': passwords})
    return render(request, 'password_generator/generate_passwords.html')
'''
def recover_passwords_view(request):
    if request.method == 'POST':
        names = [request.POST.get(f"original_favourite_word_{i + 1}") for i in range(5)]
        numbers = [request.POST.get(f"original_favourite_number_{i + 1}") for i in range(2)]
        key = request.POST.get('key')
        passwords = request.session.get('passwords')
        if key and key == request.session.get('key'):
            recovered_passwords = []
            for i, password in enumerate(passwords):
                words = ''.join(names)
                number = ''.join(numbers)
                password = password.replace(number, "")
                password = password.replace(words.lower(), "")
                password = password.replace(words.upper(), "")
                password = password.replace(words.capitalize(), "")
                password = password.replace(words.title(), "")
                password = password
				'''
				
def recover_passwords_view(request):
    if request.method == 'POST':
        names = [request.POST.get(f"original_favourite_word_{i + 1}") for i in range(5)]
        numbers = [request.POST.get(f"original_favourite_number_{i + 1}") for i in range(2)]
        key = request.POST.get('key')
        passwords = request.session.get('passwords')
        if key and key == request.session.get('key'):
            recovered_passwords = []
            for i, password in enumerate(passwords):
                words = ''.join(names)
                number = ''.join(numbers)
                password = password.replace(number, "")
                password = password.replace(words.lower(), "")
                password = password.replace(words.upper(), "")
                password = password.replace(words.capitalize(), "")
                password = password.replace(words.title(), "")
                password = "".join(random.sample(password, len(password)))
                password = password[:12]
                recovered_passwords.append(password)
            return render(request, 'password_generator/recovered_passwords.html', {'recovered_passwords': recovered_passwords})
    return render(request, 'password_generator/recover_passwords.html')
