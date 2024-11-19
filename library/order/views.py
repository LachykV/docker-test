from datetime import timedelta

from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import OrderForm
from book.models import Book
from order.models import Order
from utils.permissions import admin_check


@login_required
def orders_view(request):
    if admin_check(request.user):
        orders = Order.objects.filter(end_at=None)
        return render(request, 'order/orders_list_admin_view.html', {'orders': orders})
    else:
        user_orders = Order.objects.filter(user=request.user, end_at=None)
        return render(request, 'order/orders_list_user_view.html', {'orders': user_orders})


@login_required
def create_order(request, book_id=None):
    # If book_id is provided, fetch the corresponding book
    book = None
    if book_id:
        book = get_object_or_404(Book, id=book_id)

    # Set the planned end date 14 days from now
    plated_end_at = timezone.now() + timedelta(days=14)

    # If this is a POST request, process the form data
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Use the book from the URL parameter if available; otherwise, use the form's selected book
            selected_book = book if book else form.cleaned_data['book']
            order = Order.create(user=request.user, book=selected_book, plated_end_at=plated_end_at)
            if order:
                return redirect('orders_view')
            else:
                return render(request, 'order/order_create_by_user.html',
                              {'error': 'Unable to create order. The book might already be reserved.', 'form': form})
    else:
        # Pre-fill the form with the selected book if book_id is provided
        initial_data = {'book': book} if book else {}
        form = OrderForm(initial=initial_data)

    return render(request, 'order/order_create_by_user.html', {'form': form})


@user_passes_test(admin_check)
def close_order(request, order_id):
    target_order = get_object_or_404(Order, pk=order_id)
    target_order.end_at = timezone.now()  # Встановлюємо дату закриття замовлення
    target_order.save()
    return redirect('orders_view')  # Перенаправлення до списку замовлень
