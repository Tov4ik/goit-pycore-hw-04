# Завдання 1 
# def total_salary(path):
#     try:
#         with open(path, encoding="utf-8") as file:
#             total = 0
#             count = 0
#             for line in file:
#                 line = line.strip()
#                 parts = line.split(",")
#                 if len(parts) != 2:
#                     continue
#                 salary = int(parts[1])
#                 total += salary
#                 count += 1

#             if count == 0:
#                 return (0, 0)
#             average = total / count
#             return (total, average)

#     except FileNotFoundError:
#         print("Файл не знайдено. Перевірте шлях.")
#         return (0, 0)


# total, average = total_salary("salary.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# **********************************************************************

# Завдання 2 

# def get_cats_info(path):
#     cats = []
#     try:
#         with open(path, encoding="utf-8") as file:
#             for line in file:
#                 line = line.strip()
#                 parts = line.split(",")
#                 if len(parts) != 3:
#                     continue
#                 cat_id = parts[0]
#                 name = parts[1]
#                 age = parts[2]
#                 cat = {"id": cat_id, "name": name, "age": age}
#                 cats.append(cat)
#         return cats

#     except FileNotFoundError:
#         print("Файл не знайдено. Перевірте шлях.")
#         return []

# cats_info = get_cats_info("cats.txt")
# print(cats_info)

# **********************************************************************

