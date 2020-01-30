from django.shortcuts import render


def main(request):

    print("1_2_3_4_5")

    return render(request, 'main/main.html', locals())
