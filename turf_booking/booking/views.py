from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib import messages

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
        phone = request.POST.get('phone')
        booking = Booking.objects.filter(phone=phone).first()

        if booking:
            booking.delete()
            messages.success(request, "✅ Booking canceled successfully.")
        else:
            messages.error(request, "❌ No booking found with this phone number.")

        return redirect('cancel_booking')

    return render(request, 'booking/cancel_booking.html')
