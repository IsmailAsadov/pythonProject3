class toys:
    ToysF = []
    ToysM = []
class dogs(nickname = None):
    def __init__(self):
        self.nickname = nickname
foofy = dogs("Foofy")
max = dogs("Max")
toys_to_inputF = input("Choose a toy for Foofy")
toys.ToysF.append(toys_to_inputF)
toys_to_inputM = input("Choose a toy for Max")
toys.ToysM.append(toys_to_inputM)