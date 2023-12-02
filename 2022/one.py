
def read_file(handle: str):
  with open(handle, "r") as f:
    return f.read()

def main():
  contents = read_file("one.input.txt")
  contents = contents.split("\n\n")
  contents = [map(int, inner.split("\n")) for inner in contents]
  contents = list(map(sum, contents))
  value_a = max(contents)
  print(f"Calories (part a): {value_a}")

  contents = sorted(contents, reverse=True)
  value_b = sum(contents[:3])
  print(f"Calories (part b): {value_b}")

if __name__ == "__main__":
  main()