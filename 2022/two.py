def read_file(handle: str):
  with open(handle, "r") as f:
    return list(map(lambda x: x.strip(), f.readlines()))
  
A = X = "Rock"
B = Y = "Paper"
C = Z = "Scissors"

# Points
WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
  contents = read_file("two.input.txt")
  for line in contents:
    opp, you = line.split(" ")
    

if __name__ == "__main__":
  main()