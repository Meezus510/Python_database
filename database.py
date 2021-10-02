import sys

print("This is the name of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("The arguments are:" , str(sys.argv))

class Account:

    def __init__(self, account, type, data):
        
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

        self.add_info(type, data)



    def add_info(self, type, data):
        
        if type == 'business_type':
            self.business_type = data
        elif type == 'country':
            self.country = data
        elif type == 'first_name':
            self.first_name = data
        elif type == 'last_name':
            self.country = data
        elif type == 'first_name_kana':
            self.first_name_kana = data
        elif type == 'last_name_kana':
            self.last_name_kana = data
        elif type == 'date_of_birth':
            self.country = data
        elif type == 'social_security_number':
            self.social_security_number = data
        elif type == 'email':
            self.email = data
        elif type == 'name':
            self.name = data
        elif type == 'director_name':
            self.director_name = data
        elif type == 'employer_id_number':
            self.employer_id_number = data
        elif type == 'support_email':
            self.support_email = data
        elif type == 'phone':
            self.phone = data
        elif type == 'tax_id_number':
            self.tax_id_number = data

def process_data(data):

    #list to hold accounts
    account_list = {}

    #loop list of entries
    for i in data:

        #split entries into  substrings
        strings = i.split(',')

        #check if account name exists in accounts
        if strings[0] in account_list:

            #find account by account name
            temp_acct = account_list.get(strings[0])
            
            temp_acct.add_info(strings[1], strings[2])

            print

        else:
            #create new account if acount name does not exist
            temp_acct = Account(strings[0], strings[1], strings[2])

            #add new account to account list
            account_list[strings[0]] = (temp_acct)

    print(account_list)
    
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