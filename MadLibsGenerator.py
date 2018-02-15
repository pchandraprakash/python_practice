print("Welcome to Mad Libs Generator Game")
company_name = input("Please enter your company name: ")
offering_name = input("Please enter what you are developing: ")
target_audience = input("Please enter the target audience: ")
what_kind_of_problem = input("What kind of problem are you solving: ")
what_is_the_secret = input("What is the secret behind this solution: ")

def Madlibgen(company_name,offering_name,target_audience,what_kind_of_problem,what_is_the_secret):
    print("My company,", company_name, "is developing a(n)", offering_name, "to help", target_audience,
          "to solve", what_kind_of_problem, "by using", what_is_the_secret)
Madlibgen(company_name,offering_name,target_audience,what_kind_of_problem,what_is_the_secret)
