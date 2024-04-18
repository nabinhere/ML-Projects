import mem_profile
import random
import time

print(f"Memory (Before): {mem_profile.memory_usage_resource()}")
names = ['Ram', 'Hari', 'Sita', 'Geeta', 'Phurba']
majors = ['Science', 'Maths', 'History', 'Sociology']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield(person)

t1