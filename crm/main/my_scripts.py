from django.contrib.auth.models import Group

from main.forms import MessageForm, OrderResponseForm


def check_user_group(user, group_name):
    return Group.objects.get(name=group_name) in user.groups.all()


# def del_customers_field_based_on_group(user, order, order_message):
#     if check_user_group(user, 'client'):
#         message_form = MessageForm(instance=order_message)
#         order_form = OrderResponseForm(instance=order)
#         del order_form.fields['customers']
#     elif check_user_group(user, 'constructor'):
#         message_form = MessageForm(instance=order_message)
#         order_form = OrderResponseForm(instance=order)
#     else:
#         return None, None
#
#     return order_form, message_form
