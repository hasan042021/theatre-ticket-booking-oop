from Classes.star_cinema import Star_cinema


class Hall(Star_cinema):
    def __init__(self,hall_no,rows,cols) -> None:
        super().__init__()
        self.__hall_no=hall_no
        self.__seats=dict()
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.entry_hall(self)
    
    def entry_show(self,id,movie_name,time):
        self.__show_list.append((id,movie_name,time))
        arr = []
        for _ in range(self.__rows):
            arr.append([0 for _ in range(self.__cols)])
        self.__seats[id]=arr

    def book_seats(self,id,seats):
        if id in self.__seats:
            all_seats=self.__seats[id]
            for (r,c) in seats:
                if r>self.__rows or c>self.__cols:
                    print("\n..........error............")
                    print(f"invalid seat ({r},{c})")
                    print("..........error............\n")
                else:
                    val=all_seats[r-1][c-1]
                    if val>0:
                        print("\n..........error............")
                        print(f"({r},{c}) seat already booked")
                        print("..........error............\n")
                    else:
                        all_seats[r-1][c-1]=1
        else:
            print("\n..........error............")
            print("invalid show id")
            print("..........error............\n")
    
    def view_show_list(self):
        print('---------------------------')
        print("       List of Shows       ")
        print('---------------------------')
        for s in self.__show_list:
            date = s[2].strftime('%d/%m/%Y')
            time = s[2].strftime('%I:%M %p')
            print(f"Name: {s[1]}   Id: {s[0]}   Date: {date}  Time: {time}")
        print('---------------------------')
     
    
    def view_available_seats(self,id):
        if id in self.__seats:
            print('---------------------------')
            print("Available seats\n")
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__seats[id][i][j] == 0:
                        print((i+1, j+1))
            print("\nupdated matrix list\n")
            for i in range(self.__rows):
                print(self.__seats[id][i]) 
            print('---------------------------')
                    
        else:
            print("\n..........error............")
            print("invalid id")
            print("..........error............\n")

    def __repr__(self) :
        return f'{self.__hall_no} {self.__rows} {self.__cols}'