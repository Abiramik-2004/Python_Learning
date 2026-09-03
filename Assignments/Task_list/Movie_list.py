Movie_list=[]
while True:
    print("1. Add the Movie")
    print("2. View the Movie list")
    print("3. Remove the Movie")
    print("4. Count the Movies")
    print("5. Exit ")
    choice=int(input("Enter the task: "))
    if( choice==1):
        movie=input("Enter a movie: ")
        Movie_list.append(movie)
        print("Movie has been added")
    elif choice==2:
        if(len(Movie_list)==0):
            print("There is no item in the list")
        else:
            print(Movie_list)
    elif choice==3:
        movie=input("enter the item to remove: ")
        if movie in Movie_list:
            Movie_list.remove(movie)
            print("movie is removed")
        else:
            print("movie not present")
    elif choice==4:
        print("No of movies present in a list: ",len(Movie_list))
    else:
        exit(0)

