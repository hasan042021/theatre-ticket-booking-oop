from datetime import datetime,timedelta
from Classes.hall import Hall
from Classes.star_cinema import Star_cinema

cineplex=Hall(2,6,6)
cineplex.entry_show(11,"Batman begins",datetime.now()- timedelta(seconds=1000))
cineplex.entry_show(12,"The dark night",datetime.now()+ timedelta(seconds=19000))
cineplex.entry_show(13,"The dark night rises",datetime.now()- timedelta(seconds=20000))




while(True):
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    op=int(input("ENTER OPTION: "))
    if(op==1):
        cineplex.view_show_list()
    elif op==2:
        id=int(input("Enter show id: "))
        cineplex.view_available_seats(id)
    elif op==3:
        id=int(input("Enter show id: "))
        n=int(input("Number of tickets: "))
        seats=[]
        for i in range(n):
            r=int(input(f"row:"))
            c=int(input(f"column: "))
            seats.append((r,c))
            if i < n-1:
                print("next ticket")
        cineplex.book_seats(id,seats)
    else:
        break


