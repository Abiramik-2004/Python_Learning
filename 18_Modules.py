'''
Modules:
    A module is a python file (.py) containing variables, functions, classes,or statements that can e reused in another python program.
    Uses:
    -----
        reusability
        Organization
        Maintainability
        Namespace management
    
    WAYS TO IMPORT:
    ---------------
        -> Import the cmplete module:
            import math
        -> Import specific function:
            from math import sqrt
        -> Import with an alias:
            import math as m
        -> Import multiple names:
            from math import sqrt,factorial
    
    Standard library modules:
    -------------------------
    Python provides many ready-to-use modules.
    ex:
        math for mathematical operations
        random for randomvalues
        datetime for date and times
        os for Opeating system
        json for JSON data
    
    __name__=='__main__'
    ----------------------
    This condition makes code run only when the file is executed directly, not when it is imported as a module.

    def greet():
        prin("Hello")
    if __name__=="__main__"
        greet()

'''