from rest_framework import serializers
from listings.models import Listing, PointInterest, Booking
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point


class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    seller_profile_picture = serializers.SerializerMethodField()
    listing_pois_within_radius = serializers.SerializerMethodField()
    listing_within_radius = serializers.SerializerMethodField()
    bookings = serializers.SerializerMethodField()
    booked_dates = serializers.SerializerMethodField()

    def get_bookings(self, obj):
        queryset = Booking.objects.filter(listing=obj)
        serialized_data = BookingSerializer(queryset, many=True).data
        return serialized_data

    def get_booked_dates(self, obj):
        queryset = Booking.objects.filter(listing=obj, status='Approved')
        serialized_data = BookingSerializer(queryset, many=True).data

        # Modify the serialized data to only include the date_booked field for each approved booking
        serialized_data = [booking['date_booked']
                           for booking in serialized_data if booking['status'] == 'Approved']

        return serialized_data

    def get_listing_within_radius(self, obj):
        try:
            query = Listing.objects.filter(
                latitude__range=(obj.latitude - 0.04, obj.latitude + 0.04),
                longitude__range=(obj.longitude - 0.04, obj.longitude + 0.04)
            ).order_by('-id')
            query_serialized = NearbySerializer(query, many=True)
            return query_serialized.data
        except AttributeError as e:
            print("err", e)
            return None

    def get_listing_pois_within_radius(self, obj):
        try:
            listing_location = Point(obj.latitude, obj.longitude, srid=4326)
            query = PointInterest.objects.filter(
                location__distance_lt=(listing_location, D(km=1.01)))
            query_serialized = PoiSerializer(query, many=True)
            return query_serialized.data
        except AttributeError as e:
            print("err", e)
            return None

    def get_seller_agency_name(self, obj):
        try:
            return obj.seller.profile.agency_name
        except AttributeError as e:
            print("AttributeError:", e)
            return None

    def get_seller_profile_picture(self, obj):
        try:
            return obj.seller.profile.profile_picture.url
        except AttributeError as e:
            print("Attr Error", e)
            return None

    def get_seller_username(self, obj):
        try:
            return obj.seller.username
        except AttributeError as e:
            print("AttributeError:", e)
            return None

    def get_country(self, obj):
        return "Nepal"

    class Meta:
        model = Listing
        fields = '__all__'


class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointInterest
        fields = '__all__'


class NearbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    booker_profile_picture = serializers.SerializerMethodField()

    def get_booker_profile_picture(self, obj):
        try:
            return obj.booker.profile.profile_picture.url
        except AttributeError as e:
            print("Attr Error", e)
            return None

    class Meta:
        model = Booking
        fields = '__all__'


class BookingStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status', 'rating']
