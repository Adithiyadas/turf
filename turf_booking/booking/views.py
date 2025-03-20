


from django.shortcuts import render, redirect
from .forms import BookingForm, CancelBookingForm
from .models import Booking

def book_turf(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            slot_prices = {'6am-7am': 500, '7am-8am': 750, '8am-9am': 1000}
            booking = form.save(commit=False)
            booking.amount = slot_prices[booking.time_slot]
            booking.save()
            return render(request, 'booking/confirmation.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking/turf_form.html', {'form': form})

def cancel_booking(request):
    if request.method == "POST":
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            booking = Booking.objects.filter(phone=phone).first()
            if booking:
                booking.delete()
                return render(request, 'booking/cancel_success.html', {'phone': phone})
            else:
                return render(request, 'booking/cancel_fail.html', {'phone': phone})
    else:
        form = CancelBookingForm()
    return render(request, 'booking/cancel_form.html', {'form': form})
