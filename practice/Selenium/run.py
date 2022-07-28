from booking.booking import Booking
import time

# using context manager to make sure the file is closed after being used. basically, it creates a 'session' with the file
with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency = 'USD')
    bot.select_place_to_go('Florianópolis')
    bot.select_dates(check_in_date='2022-03-01',
                    check_out_date='2022-03-15')
    bot.select_adults(5)
    bot.click_search()