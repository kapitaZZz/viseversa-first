from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	usertext = request.GET['usertext']
	reversed_text = usertext[::-1]
	words_in_string = usertext.split()
	temp_len = len(words_in_string)
	print(words_in_string)
	print(temp_len)
	return render(request, 'reverse.html', {'usertext': usertext,
											'reversed_text': reversed_text, 
											'words_in_string': temp_len})