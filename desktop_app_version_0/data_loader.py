def load_files():
    with open('labelled_data\labelled_bedrooms_data_sample.txt.txt') as f:
        bedrooms_lines = f.readlines()
    with open('labelled_data\labelled_living_rooms_data_sample.txt.txt') as f:
        living_rooms_lines = f.readlines()
    with open('labelled_data\labelled_kitchens_data_sample.txt.txt') as f:
        kitchens_lines = f.readlines()
    with open('labelled_data\labelled_dining_data_sample.txt.txt') as f:
        dining_lines = f.readlines()
    with open('labelled_data\labelled_bathrooms_data_sample.txt.txt') as f:
        bathrooms_lines = f.readlines()
    bedroom_files = []
    for bedroom_line in bedrooms_lines:
        bedroom_files.append(bedroom_line.split("; ")[0])
    bedrooms = []
    for bedroom_line in bedrooms_lines:
        bedrooms.append(bedroom_line.split("; ")[2:])
    living_rooms_files = []
    for living_room_line in living_rooms_lines:
        living_rooms_files.append(living_room_line.split("; ")[0])
    living_rooms = []
    for living_room_line in living_rooms_lines:
        living_rooms.append(living_room_line.split("; ")[2:])
    kitchens_files = []
    for kitchen_line in kitchens_lines:
        kitchens_files.append(kitchen_line.split("; ")[0])
    kitchens = []
    for kitchen_line in kitchens_lines:
        kitchens.append(kitchen_line.split("; ")[2:])
    dining_files = []
    for dining_line in dining_lines:
        dining_files.append(dining_line.split("; ")[0])
    dining = []
    for dining_line in dining_lines:
        dining.append(dining_line.split("; ")[2:])
    bathroom_files = []
    for bathroom_line in bathrooms_lines:
        bathroom_files.append(bathroom_line.split("; ")[0])
    bathrooms = []
    for bathroom_line in bathrooms_lines:
        bathrooms.append(bathroom_line.split("; ")[2:])
        
    return bedroom_files, bedrooms, living_rooms_files, living_rooms, kitchens_files, kitchens, dining_files, dining, bathroom_files, bathrooms



