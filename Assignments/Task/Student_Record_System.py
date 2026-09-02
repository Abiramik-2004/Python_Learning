Students=((101,"Abi","Java",85),
          (102,"Bhaskar","J2EE",90),
          (103,"Navi","C#",90),
          (104,"Savi","python",80))
while(True):
    print("1.Display Students")
    print("2.Search Student")
    print("3.Highest Mark")
    print("exit")
    n=int(input("Enter Choice"))
    if(n==2):
        print(Students)
        id=int(input("Enter id"))
        for i in Students:
            if(Students[i][0]==id):
                print(i)
                break
            
        