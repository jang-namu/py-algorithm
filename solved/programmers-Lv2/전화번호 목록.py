def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    min_length = len(phone_book[0])
    phone_hash = set()

    for phone in phone_book:
        phone_length = len(phone)
        if min_length > phone_length:
            min_length = phone_length
        for i in range(min_length, phone_length + 1):
            if phone[:i] in phone_hash:
                return False
        phone_hash.add(phone)

    return True