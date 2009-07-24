def liveblog_order(request):
    valid_orders = {'asc': '-pub_date',
                    'desc': 'pub_date', }
    order = valid_orders['asc'] # default
    if request.GET:
        if request.GET.has_key('order'):
            selected_order = request.GET['order']
            if selected_order in valid_orders.keys():
                order = valid_orders[selected_order]
    return {'liveblog_order': order, }
