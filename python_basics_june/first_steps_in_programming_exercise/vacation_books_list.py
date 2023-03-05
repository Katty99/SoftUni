total_number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days_to_read_a_book = int(input())
hours_to_read_a_book = total_number_of_pages / pages_per_hour
hours_per_day = hours_to_read_a_book / number_of_days_to_read_a_book
print(int(hours_per_day))