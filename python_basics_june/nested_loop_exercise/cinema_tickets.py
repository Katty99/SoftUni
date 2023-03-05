command = input()
students_ticket_counter = 0
standard_tickets_counter = 0
kids_ticket_counter = 0

while command != 'Finish':
    free_seats = int(input())
    sold_tickets_counter = 0
    total_seats_in_the_hall = free_seats
    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'standard':
            standard_tickets_counter += 1
        elif ticket_type == 'student':
            students_ticket_counter += 1
        elif ticket_type == 'kid':
            kids_ticket_counter += 1
        free_seats -= 1
        sold_tickets_counter += 1
    percent_busy = sold_tickets_counter / total_seats_in_the_hall * 100
    print(f'{command} - {percent_busy:.2f}% full.')
    command = input()
total_tickets_sold = standard_tickets_counter + students_ticket_counter + kids_ticket_counter
standard_tickets_percent = standard_tickets_counter / total_tickets_sold * 100
students_ticket_percent = students_ticket_counter / total_tickets_sold * 100
kids_ticket_percent = kids_ticket_counter / total_tickets_sold * 100
print(f'Total tickets: {total_tickets_sold}')
print(f'{students_ticket_percent:.2f}% student tickets.')
print(f'{standard_tickets_percent:.2f}% standard tickets.')
print(f'{kids_ticket_percent:.2f}% kids tickets.')



