from random import choice

print("-----------BLOOD DONATION CAMP REGISTRY MINI PROJECT(31)-----------")
#list to store all donors records
donors=[]

#login page

def login():
    print("----Blood Donation Camp Registry Login----")
    password=input("Enter password (password is pass):")
    if password=="pass":
        print("Login successful. Welcome!")
        return True
    else:
        print("Login failed.(Please enter correct details)")
        return False

#code to add  a new donor in the data

def add_donor():
    print("\n___ 1. Add New Donor___")
    name=input("Enter Name:")
    blood_grp=input("Enter blood grp(like A+,A-,AB,O+):")
    age=int(input("Enter age:"))
    weight=float(input("Enter weight in Kg:"))
    months_since_last=int(input("Enter months since last donated:"))
    contact=input("Enter Contact Number:")
#creating a dict for the new donor
    new_donor={"name":name,"blood_grp":blood_grp,"age":age,"weight":weight,"months_since_last_donated":months_since_last,"contact":contact}
    donors.append(new_donor)
    print(f"Successfully added donor:{name}")

#code to view the details of a donor

def view_donor():
    print("\n--- 2.View All Donors ---")
    if not donors:
        print("No donor in the registry yet.")
        return

    print(f"Total Donors:{len(donors)}")
    print("-" * 20)
#For loop through the list to print details from each dictionary
    for donor in donors:
        print(f"Name:{donor['name']}")
        print(f"Age:{donor['age']}")
        print(f"Weight:{donor['weight']}")
        print(f"Blood Group:{donor['blood_grp']}")
        print(f"Last Donation:{donor['months_since_last_donated']}")
        print(f"Contact:{donor['contact']}")
        print("-" * 20)

#code to search donor
def search_donor():

    print("\n--- 3. Search for Donor")
    if not donors:
        print("No donors in the registry to search.")
        return
    search_name=input("Enter the name of the donor to find: ").strip().lower()
    found_donor=None
#For loop through the list to search for the donor
    for donor in donors:
        if donor['name'].strip().lower()==search_name:
            found_donor=donor
            break
    if found_donor:
        print("---DONOR FOUND---")
        print(f"Name: {found_donor['name']},Age: {found_donor['age']},Weight:{found_donor['weight']}kg,Blood Group:{found_donor['blood_grp']}")
    else:
        print(f"|||No donor found with this name{search_name}.|||Plz enter correct details|||")

#code to modify details for a Donor

def modify_donor():
    print("\n---4. Modify Donor Details--- ")
    if not donors:
        print("No donors in the registry to modify.")
        return
    search_name=input("Enter the name of the Donor you want to modify.").strip().lower()
    donor_to_modify=None
#For loop through the list to search for the donor
    for donor in donors:
        if donor['name'].strip().lower()==search_name:
            donor_to_modify=donor
            break
    if donor_to_modify:
        print(f"Modifying donor:{donor_to_modify['name']}.Leave blank if you dont want to change the name.")
#mostly people will modify contact no,age and weight
    new_contact=input("Enter New Contact:")
    if new_contact:
        donor_to_modify['contact']=new_contact
    print("___CONTACT DETAILS CHANGED___")
    new_weight=float(input("Enter New Weight in Kg:"))
    if new_weight:
        donor_to_modify['weight']=new_weight
    print("---WEIGHT HAS BEEN UPDATED---")
    new_age=int(input("Enter Current Age:"))
    if new_age:
        donor_to_modify['age']=new_age
    print("---AGE HAS BEEN UPDATED---")
    print("|||DETAILS HAS BEEN SUCCESSFULLY UPDATED|||")

#code to delete details of a donor

def delete_donor():
    print("\n 5. Delete A Donor Record.")
    if not donors:
        print("No donors in the registry to delete.")
        return
    search_name=input("Enter the name of the donor to delete its record:").strip().lower()
    donor_to_delete=None
    for donor in donors:
        if donor['name'].strip().lower()==search_name:
            donor_to_delete=donor
            break
    if donor_to_delete:
        confirm=input(f"Are u sure u want to delete {donor_to_delete['name']}? (y/n):").lower()
        if confirm=='y':
            donors.remove(donor_to_delete) # remove the dictonary of the donor
        else:
            print("Deletion cancelled")
    else:
        print(F"No Donor found with the name {search_name}")

#code to check donor eligibility

def generate_report():
    print("\n--- 6. Generate Reports---")
    if not donors:
        print("No data to generate report.")
        return
    print("---Donor Eligibility Report---")
    eligible_names=[]
    for donor in donors:
        is_age_eligible=18<= donor['age']<=60
        is_weight_eligible=donor['weight']>=50
        is_last_donation_eligible=donor['months_since_last_donated']>=3
        if is_age_eligible and is_weight_eligible and is_last_donation_eligible:
            eligible_names.append(donor['name'])
    print(f"Eligible:{eligible_names}")

#code to generate  main menu
def main_menu():
    while True:
        print("\n=====================================")
        print("Blood Donation Camp Registry")
        print("\n=====================================")
        print("1. Add New Donor")
        print("2.View All Donors")
        print("3. Search for Donor")
        print("4. Modify Donor Details")
        print("5. Delete A Donor Record.")
        print("6. Generate Reports")
        print("7. Exit")
        choice=input("Enter your choice(1-7)")
        if choice=='1':
            add_donor()
        elif choice=='2':
            view_donor()
        elif choice=='3':
            search_donor()
        elif  choice=='4':
            modify_donor()
        elif choice=='5':
            delete_donor()
        elif choice=='6':
            generate_report()
        elif  choice=='7':
            print("Exiting Program!!. Goodbye")
            break
        else:
            print("Invalid Choices.Please choice a number between 1 and 7")
if __name__=="__main__":
    if login():
        main_menu()
    else:
        print("Login Failed.")







