from django.shortcuts import render, redirect
from Cash.models import Cash

import math

INV = 0
RATE = 0
POW = 1
MULTI = 1
RESULT = 0


def check_string(strring):
    if strring:
        return True
    return False


# Create your views here.
def index(request):
    items = Cash.objects.all()

    sum_inv = sum(i.investment for i in items)
    sum_share = sum(i.share for i in items)
    avg = sum_inv / sum_share

    return render(request, 'Cash/index.html', context={
        'sum_inv': round(sum_inv, 2),
        'sum_share': round(sum_share, 4),
        'avg': round(avg, 4),
        'sum_fee': sum(i.fee for i in items),
        'inv': INV,
        'rate': RATE,
        'pow': POW,
        'multi': MULTI,
        'result': RESULT
    })


def edit_form(request):
    if request.method == 'POST':
        pk = request.POST.get('item_pk')
        if pk == '0':
            c = Cash()
        else:
            c = Cash.objects.get(pk=int(pk))

        inv = request.POST.get('item_inv')
        if check_string(inv):
            c.investment = round(float(inv), 2)

        worth = request.POST.get('item_worth')
        if check_string(worth):
            c.worth = round(float(worth), 4)

        share = request.POST.get('item_share')
        if check_string(share):
            c.share = round(float(share), 4)

        fee = request.POST.get('item_fee')
        if check_string(fee):
            c.fee = round(float(fee), 2)

        date = request.POST.get('item_date')
        if check_string(date):
            c.created_time = date

        c.save()

    return redirect('Cash:index')


def new_form(request):
    global RATE
    global INV
    global POW
    global MULTI
    global RESULT

    if request.method == 'POST':
        inv = request.POST.get('new_inv')
        rate = request.POST.get('new_rate')
        pow = request.POST.get('new_pow')
        multi = request.POST.get('new_multi')

        if check_string(inv):
            INV = float(inv)

        if check_string(rate):
            RATE = float(rate)

        if check_string(pow):
            POW = float(pow)

        if check_string(multi):
            MULTI = float(multi)

        sum_inv = sum(i.investment for i in Cash.objects.all())
        delta = sum_inv * math.pow(((RATE / 100) * MULTI), POW)

        RESULT = round(INV - delta, 2)

    return redirect('Cash:index')
