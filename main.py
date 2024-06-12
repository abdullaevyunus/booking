from pprint import pprint


def get_city():
    """Shaxar tanlash uchun
    :return: str
    """
    message = 'Shahringizni kiriting: '
    cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Xorazm', 'Andijon']  # Mavjud shahar nomlari

    while True:
        city = input(message)
        if city == 'exit':
            return None

        if city in cities:
            return city
        else:
            print('Bizda bunday shahar yoq')


def get_booking():
    """
    Band qilish uchun joy tanlash
    :return: str
    """
    message = 'Nma band qilmoqchisiz: '
    booking_type = ['Hotel', 'Apartments']  # Mavjud xizmat nomlari

    while True:
        print(booking_type)
        book = input(message)
        if book == 'exit':
            return None

        if book in booking_type:
            return book
        else:
            print('Bizda bunday xizmat mavjud emas!')


def get_hotel():
    """
    Mehmon hona nomini tanlash
    :return: str
    """
    message = ('Mehmonhonani tanlang: ')

    hotels = ['Wyndham', 'Radison', 'Hyatt', "O'zbekiston Hotel"]  # Mavjud mehmonhonalar

    while True:
        print(hotels)
        hotel = input(message)
        if hotel == 'exit':
            return None

        if hotel in hotels:
            return hotel
        else:
            print('Bizda bunday mehmonhona mavjud emas: ')


def get_apartments():
    """
    Apartament turini tanlash
    :return: str
    """

    message = 'Apartments tanlang: '

    apartments = ['Golden Hous', 'Murad Buildings', 'Dream Hous']  # Mavjud apartamantlar

    while True:
        print(apartments)
        apartment = input(message)
        if apartment == 'exit':
            return None

        if apartment in apartments:
            return None
        else:
            print('Bizda bunday appartamenet mavjud emas: ')


def get_hotel_room_type():
    """
    Hotel xona turini tanlash
    :return: str
    """
    room_types = ['standard', 'yarim lyuks', 'lyuks']
    message = 'xona turini tanlang: '

    while True:
        print(room_types)
        room_type = input(message)
        if room_type == 'exit':
            return None

        if room_type in room_types:
            return room_type
        else:
            print('Bizda bunday turdagi xona mavjud emas')


def get_hotel_room_number():
    """
    Hotel xona raqamini tanlash
    :return: int
    """
    rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    message = 'Xona raqamini tanlang: '

    while True:
        print(rooms)
        room = int(input(message))

        if room == 'exit':
            return None

        try:
            if room in rooms:
                return room
            else:
                print('Bu xona band')
        except ValueError:
            print('Iltimos raqam kiriting')


def get_apartment_type():
    """
    Appartment xona sonini tanlash
    :return: int
    """
    message = 'Nechta xonali xonadon: '
    apartment_types = [1, 2, 3, 4]

    while True:
        print(apartment_types)
        apartment_type = int(input(message))

        if apartment_type == 'exit':
            return None

        try:
            if apartment_type in apartment_types:
                return apartment_type
            else:
                print("Bizda bunday turdahi xonodon yo'q")
        except ValueError:
            print('Iltimos raqam kiriting!')


def get_apartment_level():
    """
    Apartment qavatini tanlash
    :return: int
    """

    message = 'Xonadon qavatini tanlang: '
    levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    while True:
        print(levels)
        level = int(input(message))

        if level == 'exit':
            return None

        try:
            if level in levels:
                return None
            else:
                print('Bizda bunday qavat mavjud emas')
        except ValueError:
            print('Iltimos raqam kiriting')


def get_booking_deatils():
    firstd_day = input('Kelish sanasi(dd-mm-yyyy): ')
    last_day = input('Ketish sanasi(dd-mm-yyyy): ')
    return {
        'kelish sanasi': firstd_day,
        'ketish sanasi': last_day,
    }


def get_user_details():
    name = input('ismingizni kiriting: ')
    phone = input('telefon raqamingizni kiriting: ')
    return {
        'ism': name,
        'telefon': phone,
    }


def main():
    city = get_city()
    if city is None:
        return

    booking = get_booking()
    if booking is None:
        return

    if booking == 'Hotel':
        booking_type = get_hotel()

        if booking_type is None:
            return

        room_type = get_hotel_room_type()
        if room_type is None:
            return

        room_number = get_hotel_room_number()
        if room_number is None:
            return
    else:
        booking_type = get_apartments()
        if booking_type is None:
            return

        room_type = get_apartment_type()
        if room_type is None:
            return

        room_number = get_apartment_level()
        if room_number is None:
            return

    details = get_booking_deatils()
    user = get_user_details()

    all_details = {
        'foydalanuvchi': user,
        'shahar': city,
        'band qilish turi': booking,
        'Hotel/apartment': booking_type,
        'xona turi': room_type,
        'xona raqami': room_number,
        'yashash mudati': details,
    }

    pprint(all_details)


if __name__ == "__main__":
    main()
