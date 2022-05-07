# Create a program to generate fake data like name, email, or detailed fake profile with all the information about a person.

# Faker is a python package, which can be installed by using pip install Faker in the terminal. Each time you run this program faker generator, it will result in different random data.

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())
print(fake.country())

print(fake.profile())                                                        