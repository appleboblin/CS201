import re

"""Find matching regular expression"""
def compute_new_office(current_office):
  office = re.search("^([A-Z]{3}\s)+([0-9]{4})$", current_office)
  if not office:
    # print(current_office)
    return current_office
  new_office = str(int(office.group(2))+1000)
  # print(office.group(1)+new_office)
  return office.group(1)+new_office

"""Run code"""
# def main():
#   office = "/KEC 3047/"
#   compute_new_office(office)


# if __name__ == "__main__":
#     main()
