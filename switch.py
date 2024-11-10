matter = int(input("matter daal: "))
def switches(matter):
    match matter:
        case 1:
            return "ye ek hai"
        case 2:
            return "ye do hai"
        case 3:
            return "ye teen hai"
        case _:
            return "default case"
print("",switches(matter))
