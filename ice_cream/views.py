from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm
import datetime
from .models import Flavor, Topping, Container
from django.core.mail import send_mail


def home_page(request):
    return render(request, 'ice_cream/home_page.html', {})


def orderview(request):
    """
    template_name = 'order.html'
    form_class = OrderForm
    success_url = '/thanks/'

    """
    if request.method == "POST":
        form = OrderForm(request.POST)

    #there may be some sort of errors attribute or raise error method for redirecting

        if form.is_valid():
            order = form.save(commit=False)
            order.order_time = datetime.datetime.now()
            order.save()

            toppings_str = ''

            for topping in form.cleaned_data.get('toppings'):
                toppings_str += str(topping) + ', '

            # get rid of final comma
            toppings_str = toppings_str[:-2]

            email_body = 'A new order for ice cream was made by ' + order.name + '.\n\n' + \
                         'Flavor: ' + order.flavor + '\n' + \
                         'Container: ' + order.container + '\n'

            # if not empty, show toppings
            if len(toppings_str) > 0:
                email_body += 'Toppings: ' + toppings_str

            send_mail('New Order', email_body,
                      'claires.icecream.order@gmail.com', ['meyer.alexander.john@gmail.com'], fail_silently=False)

            # ONCE ORDERED, SHOULD REDIRECT TO ANOTHER PAGE
            return redirect('success/')
        else:
            # Should maybe stay at the same page, with some error message? Compromise on this
            form = OrderForm()
    else:
        form = OrderForm()

    """
    def form_valid(self, form):
        form.send_email
        return super(OrderView, self).form_valid(form)
    """

    return render(request, 'ice_cream/order.html', {'form': form})


def optionview(request, option_type):

    type_model_dict = {
        'flavors': Flavor,
        'toppings': Topping,
        'containers': Container,
    }

    def get_img_dict(option_list):
        img_dict = dict()

        for option in option_list:
            pass

    option_list = type_model_dict(option_type).objects.all()
    option_img_dict = get_img_dict(option_list)

    context = {'option_list': option_list, 'image_dict': option_img_dict}
    #how to make this path just choices?
    return render(request, 'ice_cream/choices.html', context)
