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

    #used to validate accounts based on business type and country
    def validate(self):
        
        if self.business_type == None:
            return False, 'business_type'
        elif self.country == None:
            return False, 'country'
        elif self.business_type == 'company':
            self.validate_company()
        elif self.business_type == 'individual':
            self.validate_individual()

    def validate_individual(self):

        unverified_list = []

        if(self.country == 'US'): 

            if(self.first_name == None):
                unverified_list.append('first_name')
            if(self.last_name == None):
                unverified_list.append('last_name')
            if(self.date_of_birth == None):
                unverified_list.append('date_of_birth')
            if(self.social_security_number == None):
                unverified_list.append('social_security_number')
            if(self.email == None):
                unverified_list.append('email')
            if(self.phone == None):
                unverified_list.append('phone')
       
        elif(self.country == 'JP'):

            if(self.first_name == None):
                unverified_list.append('first_name')
            if(self.last_name == None):
                unverified_list.append('last_name')
            if(self.first_name_kana == None):
                unverified_list.append('first_name_kana')
            if(self.last_name_kana == None):
                unverified_list.append('last_name_kana')
            if(self.date_of_birth == None):
                unverified_list.append('date_of_birth')
            if(self.tax_id_number == None):
                unverified_list.append('tax_id_number')
            if(self.email == None):
                unverified_list.append('email')

        elif(self.country == 'FR'):

            if(self.first_name == None):
                unverified_list.append('first_name')
            if(self.last_name == None):
                unverified_list.append('last_name')
            if(self.tax_id_number == None):
                unverified_list.append('tax_id_number')
            if(self.email == None):
                unverified_list.append('email')
            if(self.phone == None):
                unverified_list.append('phone')

    def validate_company(self):

        unverified_list = []

        if(self.country == 'US'):

            if(self.name == None):
                unverified_list.append('name')
            if(self.employer_id_number == None):
                unverified_list.append('employer_id_number')
            if(self.support_email == None):
                unverified_list.append('support_email')
            if(self.phone == None):
                unverified_list.append('phone')

        elif(self.country == 'JP'):

            if(self.name == None):
                unverified_list.append('name')
            if(self.tax_id_number == None):
                unverified_list.append('tax_id_number')
            if(self.phone == None):
                unverified_list.append('phone')

        elif(self.country == 'FR'):

            if(self.name == None):
                unverified_list.append('name')
            if(self.director_name == None):
                unverified_list.append('director_name')
            if(self.tax_id_number == None):
                unverified_list.append('tax_id_number')
            if(self.phone == None):
                unverified_list.append('phone')

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