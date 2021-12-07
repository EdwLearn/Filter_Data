DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    
    all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
    adult = list(filter(lambda worker: worker['age'] > 18, DATA))
    adult = list(map(lambda worker: worker['name'], adult ))
    old_people = list(map(lambda worker: worker | {'old': worker['age']> 70}, DATA))
    
    #INVERSE
    #all_python_devs_2
    all_python_devs_2 = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_2 = list(map(lambda worker: worker['name'], all_python_devs_2))
    #all_platzi_workers
    all_platzi_workers_2 = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_2 = list(map(lambda worker: worker['name'], all_platzi_workers_2 ))
    #adult
    adult_2 = [worker['name'] for worker in DATA if worker['age'] > 18]
    #old_people
    old_people_2 = [worker | {'old': worker['age']> 70} for worker in DATA]
    #old_people_2 = list(map(lambda worker: worker['old'], old_people_2))
    old_people_2 = [worker['old'] for worker in old_people_2]
    
    

    print("------------Python------------")
    for worker in all_python_devs:
        print(worker)   
    print("--------------Platzi-------------")
    for worker in all_Platzi_workers:
        print(worker)
    print("----------Age > 18----------")
    for worker in adult:
        print(worker)
    print("------------old------------")
    for worker in old_people:
        print(worker)
        
    print("-----------INVERSE--------------")
    print("------------Python------------")
    for worker in all_python_devs_2:
        print(worker)
    print("--------------Platzi-------------")
    for worker in all_platzi_workers_2:
        print(worker)
    print("----------Age > 18----------")
    for worker in adult_2:
        print(worker)
    print("------------old------------")
    for worker in old_people_2:
        print(worker)

if __name__ == '__main__':
    run()