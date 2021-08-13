from dog import Dog

def main():
    dog1 = Dog("Spike the Sleepy", 5, "Bull Dog")   # create a Dog object
    dog2 = Dog("Energy the Excited", 7, "Corgi")
    dog3 = Dog("Yuki the Lucky", 4, "Shiba Inu")
    dog4 = Dog("Nian the Aloof", 6, "Chow Chow")

    name_to_dog = { "spike" : dog1, "energy": dog2, "yuki": dog3, "nian": dog4 }

    print("---Original name_to_dog---")
    print_dogs(name_to_dog)
    print()

    name_to_dog_copy = name_to_dog.copy()    # shallow copy
    print("---Copy of name_to_dog---")
    print_dogs(name_to_dog_copy)
    print()

    name_to_dog_copy["yuki"].age += 10    # altering the yuki on copy? or just copy?

    print("---After altering age in copy, Original name_to_dog---")
    print_dogs(name_to_dog)
    print()

    print("---After altering age in copy, Copy name_to_dog---")
    print_dogs(name_to_dog_copy)
    print()


def print_dogs(name_to_dog):
    for name, dog in name_to_dog.items():
        print(f"{name} - {dog}")


if __name__ == '__main__':
    main()