from django.shortcuts import render, redirect
import datetime
import random
from .forms import MyForm
from .models import Submission

def index(request):
    current_time = datetime.datetime.now()
    
    context = {'current_time': current_time}
    return render(request, 'index.html', context)

def quote(request):
    random_quote = get_random_quote()
    context = {'random_quote': random_quote}
    return render(request, 'quote.html', context)


def form_submission(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            submission = Submission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            
            submission.save()            

            # Redirect to a new page displaying all submitted data
            return redirect('submission_list')
    else:
        form = MyForm()

    return render(request, 'form_submission.html', {'form': form})


def submission_list(request):
    # Retrieve all submissions from the database
    submissions = Submission.objects.all()
    return render(request, 'submission_list.html', {'submissions': submissions})    

def contactUs(request):
    return render(request, 'contactUs.html')

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. -Theodore Roosevelt"
    ]

    return random.choice(quotes)