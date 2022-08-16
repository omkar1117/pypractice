
library = {}

for i in range(5):
    dept = input("Enter the Department:")
    course = input("Enter the Course:")
    subject = input("Enter the Subject:")
    author = input("Enter the Author:")

    if dept in library:
        if course in library[dept]:
            if subject in library[dept][course]:
                if author in library[dept][course][subject]:
                    print("Same author already exists")
                else:
                    library[dept][course][subject].append(author)
            else:
                library[dept][course] = {
                    subject: [author]
                }
        else:
            library[dept] = {
                course: {
                    subject: [author]
                }
            }
    else:
        library[dept] = {
            course: {
                subject: [author]
            }
        }


print("Final Library....")
print(library)
