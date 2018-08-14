# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])


def add_page_to_index(index,url,content):
    content_array = content.split()
    for context_value in content_array:
        add_to_index(index, context_value, url)


if __name__ == '__main__':
    add_page_to_index(index, 'fake.text', "This is a test")
    add_page_to_index(index, 'fake.text', "This is not a test")
    print(index)
    # [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
    # ['test',['fake.text']]]


