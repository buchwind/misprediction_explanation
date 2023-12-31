import string
from fuzzingbook.Grammars import srange, Grammar

#hotel Grammar(after normalization and multiplication to remove negative and float values)
HOTEL: Grammar = {
    "<start>": ["<hotel> <lead_time> <arrival_date_year> <arrival_date_month> <arrival_date_day_of_month> <stays_in_weekend_nights> <stays_in_week_nights> <is_repeated_guest> <previous_cancellations> <previous_bookings_not_canceled> <booking_changes> <days_in_waiting_list> <adr> <required_car_parking_spaces> <total_of_special_requests> <deposit> <family> <customers> <nights> <meal_BB> <meal_FB> <meal_HB> <meal_SC> <meal_Undefined> <market_segment_Aviation> <market_segment_Complementary> <market_segment_Corporate> <market_segment_Direct> <market_segment_Groups> <market_segment_Offline_TA_TO> <market_segment_Online_TA> <distribution_channel_Corporate> <distribution_channel_Direct> <distribution_channel_GDS> <distribution_channel_TA_TO> <distribution_channel_Undefined> <reserved_room_type_A> <reserved_room_type_B> <reserved_room_type_C> <reserved_room_type_D> <reserved_room_type_E> <reserved_room_type_F> <reserved_room_type_G> <reserved_room_type_H> <reserved_room_type_L> <reserved_room_type_P> <assigned_room_type_A> <assigned_room_type_B> <assigned_room_type_C> <assigned_room_type_D> <assigned_room_type_E> <assigned_room_type_F> <assigned_room_type_G> <assigned_room_type_H> <assigned_room_type_I> <assigned_room_type_K> <assigned_room_type_P> <customer_type_Contract> <customer_type_Group> <customer_type_Transient> <customer_type_Transient_Party>"],
    "<hotel>": ["0", "<onenine><maybe_digits>"],
    "<lead_time>": ["0", "<onenine><maybe_digits>"],
    "<arrival_date_year>": ["0", "<onenine><maybe_digits>"],
    "<arrival_date_month>": ["0", "<onenine><maybe_digits>"],
    "<arrival_date_day_of_month>": ["0", "<onenine><maybe_digits>"],
    "<stays_in_weekend_nights>": ["0", "<onenine><maybe_digits>"],
    "<stays_in_week_nights>": ["0", "<onenine><maybe_digits>"],
    "<is_repeated_guest>": ["0", "<onenine><maybe_digits>"],
    "<previous_cancellations>": ["0", "<onenine><maybe_digits>"],
    "<previous_bookings_not_canceled>": ["0", "<onenine><maybe_digits>"],
    "<booking_changes>": ["0", "<onenine><maybe_digits>"],
    "<days_in_waiting_list>": ["0", "<onenine><maybe_digits>"],
    "<adr>": ["0", "<onenine><maybe_digits>"],
    "<required_car_parking_spaces>": ["0", "<onenine><maybe_digits>"],
    "<total_of_special_requests>": ["0", "<onenine><maybe_digits>"],
    "<deposit>": ["0", "<onenine><maybe_digits>"],
    "<family>": ["0", "<onenine><maybe_digits>"],
    "<customers>": ["0", "<onenine><maybe_digits>"],
    "<nights>": ["0", "<onenine><maybe_digits>"],
    "<meal_BB>": ["0", "<onenine><maybe_digits>"],
    "<meal_FB>": ["0", "<onenine><maybe_digits>"],
    "<meal_HB>": ["0", "<onenine><maybe_digits>"],
    "<meal_SC>": ["0", "<onenine><maybe_digits>"],
    "<meal_Undefined>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Aviation>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Complementary>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Corporate>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Direct>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Groups>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Offline_TA_TO>": ["0", "<onenine><maybe_digits>"],
    "<market_segment_Online_TA>": ["0", "<onenine><maybe_digits>"],
    "<distribution_channel_Corporate>": ["0", "<onenine><maybe_digits>"],
    "<distribution_channel_Direct>": ["0", "<onenine><maybe_digits>"],
    "<distribution_channel_GDS>": ["0", "<onenine><maybe_digits>"],
    "<distribution_channel_TA_TO>": ["0", "<onenine><maybe_digits>"],
    "<distribution_channel_Undefined>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_A>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_B>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_C>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_D>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_E>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_F>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_G>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_H>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_L>": ["0", "<onenine><maybe_digits>"],
    "<reserved_room_type_P>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_A>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_B>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_C>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_D>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_E>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_F>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_G>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_H>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_I>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_K>": ["0", "<onenine><maybe_digits>"],
    "<assigned_room_type_P>": ["0", "<onenine><maybe_digits>"],
    "<customer_type_Contract>": ["0", "<onenine><maybe_digits>"],
    "<customer_type_Group>": ["0", "<onenine><maybe_digits>"],
    "<customer_type_Transient>": ["0", "<onenine><maybe_digits>"],
    "<customer_type_Transient_Party>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
