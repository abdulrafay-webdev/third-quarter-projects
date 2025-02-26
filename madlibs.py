name = input("enter name :")
place = input("enter place :")
animal = input("enter animal :")
verb = input("enter verb (action) :")
adjective = input("enter adjective :")
food = input("enter food :")

if name and animal and verb and place and adjective and food:
    story = f"""One day, {name} was walking in {place} when suddenly a giant {animal} appeared! It was {adjective} and started to {verb} all over the place.{name} was so shocked that they dropped their {food} on the ground.The {animal} looked at the {food}, sniffed it, and said, "Ew, I only eat pizza!And then it disappeared into thin air! What a weird day!"""
    
    print(story)