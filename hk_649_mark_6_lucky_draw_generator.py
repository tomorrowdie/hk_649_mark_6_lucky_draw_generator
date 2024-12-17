import random
numbers= 49 # 49 # Sets maximum number for lotter

def gen_ticket1s(is_special):
    # Function: Generate ONE mark6 ticket of 6 numbers with replacement
    # input: -
    # output: a list of 6 numbers
    # 
    ticket =[]
    # Get ticket of 7 numbers
    while len(ticket) < 7:
        draw = random.randint(1, numbers)
        if draw not in ticket:
            ticket.append(draw)
    special_number = ticket[-1]
    real_ticket = sorted(ticket[:-1])
    if is_special:
        return real_ticket+[special_number]
    else:
        return real_ticket


def gen_ticket1():
    # Function: Generate ONE mark6 ticket of 6 numbers with replacement
    # input: -
    # output: a list of 6 numbers
    # 
    ticket =[]
    while len(ticket) < 6:
        draw = random.randint(1, numbers)
        if draw not in ticket:
            ticket.append(draw)
    return sorted(ticket)

def gen_ticket2(is_special = False):
    x = list(range(1, numbers+1))
    mark6 = []
    number_to_draw = 7 #49
    for i in range(number_to_draw):
        position = random.randint(0, len(x)-1)
        mark6.append(x[position])
        x.pop(position)
    if not is_special:
        return sorted(mark6[:-1])
    else:
        return sorted(mark6[:-1])+[mark6[-1]]

def check_ticket(ticket, real_draw, special_no):
    # Function: Check ticket prize
    # inputs:
        # ticket - player's ticket
        # real_draw - Real Draw (6 numbers)
        # special_no - Special no.
    
    def check_no_match(ticket, real_draw):
        count = 0
        for no in ticket:
            if no in real_draw:
                count += 1
        return count
        
        
    special_win = special_no in ticket
    no_matches = check_no_match(ticket, real_draw)
    if no_matches == 6:
        return 'Jackpot'
    elif no_matches == 5:
        if special_win:
            return '2nd prize'
        else:
            return '3rd prize'
    else:
        return 'No prize'

def get_n_tickets(n):
    ticket_list = []
    for i in range(n):
        new_ticket = gen_ticket2(is_special=False)
        ticket_list.append(new_ticket)
    return ticket_list

n = int(input('How many tickets do you want?'))
ticket_list = get_n_tickets(n)
print(ticket_list)
draw = gen_ticket2(is_special=True)
special = draw.pop()

print(f'The draw is {draw}. Speical Number is {special}.')
print('--------------------------------')
for ticket in ticket_list:
    print(f'The ticket is {ticket}.')
    print(check_ticket(ticket, draw, special))