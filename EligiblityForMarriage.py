class EligiblityForMarriage:
    def Eligible():
        gender = input("Your Gender: ").strip().lower()
        age = int(input("Your Age: "))
        
        if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")