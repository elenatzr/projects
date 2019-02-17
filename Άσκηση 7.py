import random

def printtictactoe(p):
# Η συνάρτηση εμφανίζει την τρίλιζα, όπως δημιουργείται από τις παραμέτρους.
    print('   |   |')

    print(' ' + p[7] + ' | ' + p[8] + ' | ' + p[9])

    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + p[4] + ' | ' + p[5] + ' | ' + p[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + p[1] + ' | ' + p[2] + ' | ' + p[3])
    print('   |   |')

def decideXO():
# Η συνάρτηση επιτρέπει στον παίχτη να διαλέξει αν θα είναι X ή O.
    char = ''
    while not (char == 'X' or char == 'O'):
        print('Do you want to be X or O?')
        char = input().upper()
    if char == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def randomstart():
# Η συνάρτηση επιλέγει τυχαία ποιος θα παίξει πρώτος με την χρήση της βιβλιοθήκης random.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playagain():
# Η συνάρτηση ρωτάει τον παίχτη αν θέλει να παίξει ξανά,αφού τελείωσει το παιχνίδι.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def pmove(p, char, move):
# Η συνάρτηση καταχωρεί την κίνηση του παίχτη.
    p[move] = char

def thewin(p, char):
# Η συνάρτηση επιστρέφει αν ο παίχτης κέρδισε.
    return ((p[7] == char and p[8] == char and p[9] == char) or 
    (p[4] == char and p[5] == char and p[6] == char) or 
    (p[1] == char and p[2] == char and p[3] == char) or 
    (p[7] == char and p[4] == char and p[1] == char) or 
    (p[8] == char and p[5] == char and p[2] == char) or 
    (p[9] == char and p[6] == char and p[3] == char) or 
    (p[7] == char and p[5] == char and p[3] == char) or 
    (p[9] == char and p[5] == char and p[1] == char)) 

def copyofp(p):
# Η συνάρτηση δημιουργεί ένα αντίγραφο του πίνακα p,ώστε να την επεξεργαστόυμε, χωρίς να αλλάξει ο αρχικός πίνακας.
    ant = []
    for i in p:
        ant.append(i)
    return ant

def isavailable(p, move):
# Η συνάρτηση επιστρέφει αν η κίνηση που επέλεξε ο παίχτης είναι διαθέσιμη.
    return p[move] == ' '

def playersmove(p):
# Η συνάρτηση επιτρέπει στον παίχτη να πληκτρολογήσει την κίνησή του και ελέγχει αν αυτή είναι έγκυρη.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isavailable(p, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def themoves(p, movesList):
# Η συνάρτηση  επιστρέφει πιθανές θέσεις για κινήσεις, αν αυτές υπάρχουν.
    pmoves = []
    for i in movesList:
        if isavailable(p, i):
            pmoves.append(i)
    if len(pmoves) != 0:
        return random.choice(pmoves)
    else:
        return None

def pcmove(p,pcchar):
# Η συνάρτηση διαλέγει την κίνηση του  υπολογιστή και την επιστρέφει.
    if pcchar == 'X':
        plchar = 'O'
    else:
        plchar = 'X'
# Ελέγχει αν μπορεί ο υπολογιστής να κερδίσει στην επόμενη κίνηση.
    for i in range(1, 10):
        copy = copyofp(p)
        if isavailable(copy, i):
            pmove(copy, pcchar, i)
            if thewin(copy,pcchar):
                return i
# Ελέγχεται αν ο παίχτης κερδίζει στην επομενή του κίνηση κι αν αυτό συμβαίνει, τον σταματά.
    for i in range(1, 10):
        copy = copyofp(p)
        if isavailable(copy, i):
            pmove(copy, plchar, i)
            if thewin(copy,plchar):
                return i
# Ελέγχεται αν μία από τις γωνίες είναι διαθέσιμη.
    move = themoves(p, [1, 3, 7, 9])
    if move != None:
        return move
# Ελέγχεται αν το κέντρο είναι διαθέσιμο.
    if isavailable(p, 5):
        return 5
# Ελέγχεται αν οι πλευρές είναι διαθέσιμες.
    return themoves(p, [2, 4, 6, 8])

def isfull(p):
# Επιστρέφει αν έχει καλυφθεί όλος ο πίνακας ή οχι.
    for i in range(1, 10):
        if isavailable(p, i):
            return False
    return True


# Αρχή εκτέλεσης.
print('Welcome to Tic Tac Toe!')
while True:
# Αρχικοποίηση πίνακα
    pinakas = [' '] * 10
    plchar, pcchar = decideXO()
    who = randomstart()
    print('The ' + who + ' will go first.')
    gamestart = True
    while gamestart:
        if who == 'player':
            printtictactoe(pinakas)
            move = playersmove(pinakas)
            pmove(pinakas, plchar, move)
            if thewin(pinakas, plchar):
                printtictactoe(pinakas)
                print('Hooray! You have won the game!')
                gamestart = False
            else:
                if isfull(pinakas):
                    printtictactoe(pinakas)
                    print('The game is a tie!')
                    break
                else:
                    who = 'computer'
        else:
            move = pcmove(pinakas, pcchar)
            pmove(pinakas,pcchar, move)
            if thewin(pinakas, pcchar):
                printtictactoe(pinakas)
                print('The computer has beaten you! You lose.')
                gamestart = False
            else:
                if isfull(pinakas):
                    printtictactoe(pinakas)
                    print('The game is a tie!')
                    break
                else:
                    who = 'player'
    if not playagain():
        break
