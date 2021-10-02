import sys

print("This is the name of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("The arguments are:" , str(sys.argv))

class Account:
    def __init__(self, account):
        
        self.account = account
        self.business_type = None
        self.country = None

        #individual specific
        self.first_name = None
        self.last_name = None
        self.first_name_kana = None
        self.last_name_kana = None
        self.date_of_birth = None
        self.social_security_number = None
        self.email = None

        #company specific
        self.name = None
        self.director_name = None
        self.employer_id_number = None
        self.support_email = None

        #shared info
        self.phone = None
        self.tax_id_number = None


class Individual:
    def __init__(self, account):
        self.account = account
        self.country = None
        self.first_name = None
        self.last_name = None
        self.first_name_kana = None
        self.last_name_kana = None
        self.date_of_birth = None
        self.social_security_number = None
        self.tax_id_number = None
        self.email = None
        self.phone = None

class Companies:
    def __init__(self, account):
        self.account = account
        self.name = None
        self.director_name = None
        self.employer_id_number = None
        self.tax_id_number = None
        self.support_email = None
        self.phone = None

def process_data(data):

    for i in data:
        string = i.split(',')
        print(string)

def main():

    # Creates list of argument names
    data = sys.argv

    print(data)

    # Remove first element from arguments ie. self.py
    data.pop(0)

    print(data)

    #function to parse data and 
    process_data(data)

if __name__ == "__main__":
    main()