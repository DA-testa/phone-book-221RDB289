# python3

class Query:
    def __init__(self, query):
        if len(query) >= 2:
            self.type = query[0]
            # all phone numbers consist of decimal digits,
            # they don’t have leading zeros,
            # and each of them has no more than 7 digits
            number = int(query[1]) # converting to int removes the leading zeros
            if len(str(number)) <= 7: # checks if the number is no more than 7 digits long
                self.number = number
            if self.type == 'add' and len(query) >= 3:
                # all names are non-empty strings of latin letters,
                # and each of them has length at most 15,
                # and it’s guaranteed that there is no person with name “not found"
                name = query[2]
                if len(name) <= 15:
                    self.name = name
                

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Dictionary of all existing (i.e. not deleted yet) contacts (phone book = phone numbers with corresponding contact names).
    phone_book = {}
    for cur_query in queries:
        if hasattr(cur_query, 'type'):
            if cur_query.type == 'add':
                if hasattr(cur_query, 'number') and hasattr(cur_query, 'name'):
                    # if we already have contact with such number,
                    # we should rewrite contact's name
                    phone_book[cur_query.number] = cur_query.name
            elif cur_query.type == 'del':
                if hasattr(cur_query, 'number'):
                    # if there is no such person,
                    # then it should just ignore the query
                    if phone_book.get(cur_query.number) is not None:
                        del phone_book[cur_query.number]
            elif cur_query.type == 'find':
                if hasattr(cur_query, 'number'):
                    if phone_book.get(cur_query.number) is None:
                        response = 'not found'
                    else:
                        response = phone_book[cur_query.number]
                    result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

