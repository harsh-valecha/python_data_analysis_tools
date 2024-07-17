import requests
import json

# get request practice 
# r1 = requests.get('https://reqres.in/api/users?page=2')
# print(r1.status_code)
# print(r1.headers)

# print(r1.json())

#  get request when user not available 
# r2 = requests.get('https://reqres.in/api/users/23')
# print(r2.status_code) # 404 user is not present 

'''

    Informational responses (100 -199)
    Successful responses (200 - 299)
    Redirection messages (300 - 399)
    Client error responses (400 - 499)
    Server error responses (500 - 599)

'''


# payload = {
#     "name":"jaktap",
#     "job":"CA"
# }

# r3 = requests.post('https://reqres.in/api/users',data=payload)
# print(r3.status_code)
# id = r3.json()['id']


# # verifying if the user is created or not
# r4 = requests.get(f'https://reqres.in/api/users/{id}')
# print(r4.status_code)
# print(r4.json())

# put request
# r5 = requests.get('https://reqres.in/api/users/2')
# print(r5.json())

# # updating the user
# payload = {
#     "name":"Jaktap",
#     "job":"Cologne"
# }

# r6 = requests.put('https://reqres.in/api/users/2',data=payload)
# print(r6.status_code)
# print(r6.json())


# print(requests.get('https://reqres.in/api/users/2').json())
# payload = {
#     "job":"CA"
# }
# r7 = requests.patch('https://reqres.in/api/users/2',data=payload)
# print(r7.status_code)
# print(r7.json())


# delete

# r8 = requests.delete('https://reqres.in/api/users/2')
# print(r8.status_code,r8.text) # no content 

