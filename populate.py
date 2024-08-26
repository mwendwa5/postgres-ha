import psycopg2, random
from faker import Faker
# from brucefaker import UniqueFaker
fake = Faker()

conn = psycopg2.connect(database="employees", user="postgres", password="GvSfOyjtn9", host="127.0.0.1", port="5432")
cur = conn.cursor()

def generate_unique_random_numbers(low, high, num_numbers):
    random_gen = random.Random()
    unique_numbers = set()
    while len(unique_numbers) < num_numbers:
        unique_numbers.add(random_gen.randint(low, high))
    return list(unique_numbers)

low = 1  # adjust the lower bound as needed
high = 200000  # adjust the upper bound as needed
num_numbers = 100000
result = generate_unique_random_numbers(low, high, num_numbers)

for i in range (100000):
    # Id1 =fake.random_digit_not_null()
    # faker = UniqueFaker(Id1)
    # Id = faker()
    # Id2 = int(Id1)
    # Id3 = random.randrange(100000,500000)
    # Id2 = int(random.random())
    # Id2 = Id1+random.randrange(1,100000)
    # Id = i+Id1+Id3
    # Id = random.choice(result)+Id3
    Id = result[i]
    name = fake.name()
    name2 = fake.name()
    age=fake.random_number(digits=None)
    adress =fake.address()
    # print(Id)
    # print(i)
    # print(Id1)
    # print(Id3)
    cur.execute("INSERT INTO staff (staff_no,fname,lname,age) VALUES (%s, %s, %s, %s)", (Id, name, name2, age));
    cur.execute("INSERT INTO address (staff_no,address) VALUES (%s, %s)", (Id, adress));

conn.commit()
print("Records created successfully")
conn.close()
