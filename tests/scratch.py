# Gather package requirements
with open("requirements.txt", 'r', encoding='utf-16') as f:
    requirements = f.readlines()
print(requirements)
for string in requirements:
    print((string[:-1]))