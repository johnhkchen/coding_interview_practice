from lxml import html
import requests

# Nice-to-haves:
# Write a proper parser, rather than just pulling raw text out of the xml tree

def toSnakeCase(input):
  return input.lower().replace(" ","_");
  
def isUpper(c):
  return c > 'A' and c < 'Z'

for problemNumber in range(9, 20+1):
  problemUrl = 'https://projecteuler.net/problem='+str(problemNumber)
  #print("Connecting to {}...".format(problemUrl))
  page = requests.get(problemUrl)
  #print('Got result: {}'.format(page))
  tree = html.fromstring(page.content)
  problem_title = tree.xpath('//*[@id="content"]/h2/text()')[0]
  problem_description = tree.xpath('//*[@id="content"]/div[@class="problem_content"]/descendant::*/text()')

  print("Problem {}: {}".format(problemNumber, toSnakeCase(problem_title)))
  # print(problem_description)
  for details in problem_description:
    # clean up each line if possible
    if isUpper(details[0]):
      print()
    print(details,end='')

  print(end='\n\n')

