ceo_nested_dict = [
  {
      "name": "Warren Buffet",
      "age": 88,
      "occupation": "CEO of Berkshire Hathaway"
  },
  {
      "name": "Jeff Bezos",
      "age": 55,
      "occupation": "CEO of Amazon"
  },
  {
      "name": "Harry Markowitz",
      "age": 91,
      "occupation": "Professor of Finance"
  }
]
for index in range(len(ceo_nested_dict)):
    for key, val in ceo_nested_dict[index].items():
        print("{} : {}".format(key, val))