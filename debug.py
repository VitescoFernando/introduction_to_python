user_name = ""
user_last_name = ""
user_job_tittle = ""
age = ""
plastic_bags = ""

user_name = input('Please, write your name:')
user_last_name = input('Please, write your last name:')
user_job_tittle = input('Please, write your job title:')
age = input('Please, write your age:')
plastic_bags = input('Do you use Plastic bags? [Y] or [N]: ')
veredict = 'You are a good boy/girl'
if plastic_bags == 'Y':
    veredict = 'You are a naughty boy/girl'

print(user_name + " " + user_last_name + " " + age + " " + user_job_tittle )
print("Veredict: " + veredict)