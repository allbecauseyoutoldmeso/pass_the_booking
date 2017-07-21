from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm

def booking_list(request):
    bookings = Booking.objects.order_by('property')
    return render(request, 'pass_the_booking/booking_list.html', {'bookings': bookings })

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'pass_the_booking/booking_detail.html', {'booking': booking })

def booking_new(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'pass_the_booking/booking_edit.html', { 'form': form, 'property': property })

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    property = booking.property
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'pass_the_booking/booking_edit.html', {'form': form, 'property': property })

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    property = booking.property
    booking.delete()
    return redirect('property_detail', pk=property.pk)
