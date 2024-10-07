# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

# Answer:
def read_dictionary(file_name):
    dictionary = {}
    
    with open(file_name, 'r') as f:
        for line in f:
            word = line.strip()
            
            if len(word) >= 3:
                first_two = word[:2]
                
                if first_two not in dictionary:
                    dictionary[first_two] = []
                
                dictionary[first_two].append(word)
    
    return dictionary

# Thuật toán tìm kiếm theo chiều rộng (Breadth-First Search - BFS)
def find_shortest_chain(start_word, end_word, dictionary):
    # Khởi tạo hàng đợi với chuỗi chỉ chứa từ đầu tiên
    queue = [[start_word]]
    
    visited = set()

    # Lặp cho đến khi hàng đợi trống
    while queue:
        # Lấy ra chuỗi từ đầu tiên trong hàng đợi
        current_chain = queue.pop(0)
        
        # Lấy từ cuối cùng trong chuỗi hiện tại
        last_word = current_chain[-1]

        # Nếu từ cuối cùng là từ đích, trả về chuỗi hiện tại
        if last_word == end_word:
            return current_chain

        # Lấy hai chữ cái cuối của từ cuối cùng
        last_two = last_word[-2:]
        
        # Nếu có các từ bắt đầu bằng hai chữ cái này trong từ điển
        if last_two in dictionary:
            # Duyệt qua tất cả các từ có thể kết nối
            for next_word in dictionary[last_two]:
                # Nếu từ chưa được xét
                if next_word not in visited:
                    # Tạo một chuỗi mới bằng cách thêm từ mới vào chuỗi hiện tại
                    new_chain = current_chain + [next_word]
                    
                    # Thêm chuỗi mới vào hàng đợi
                    queue.append(new_chain)
                    
                    # Đánh dấu từ đã được xét
                    visited.add(next_word)

    # Nếu không tìm thấy chuỗi hợp lệ, trả về None
    return None

dictionary = read_dictionary('wordsEn.txt')
    
start_word = input("Enter the first word: ")
end_word = input("Enter the last word: ")

while len(start_word) < 3 or len(end_word) < 3:
    print("Words must have at least 3 letters.")
    start_word = input("Enter the first word: ")
    end_word = input("Enter the last word: ")

result = find_shortest_chain(start_word, end_word, dictionary)

if result:
    print("Shortest word chain:")
    print(" -> ".join(result))
else:
    print("No valid word chain found.")


'''
VD:
dictionary = {
    'ab': ['abc', 'abx'],
    'bc': ['bcd', 'bcz'],
    'cd': ['cde'],
    'de': ['def'],
    'xz': ['xzy'],
    'zy': ['zyx']
}

Khởi tạo:
start_word = "abc"
end_word = "def"
queue = [["abc"]]
visited = set()

Loop 1:
current_chain = ["abc"]
queue = []
last_word = "abc"
last_two = "bc"
next_word = "bcd" và "bcz"
queue = [["abc", "bcd"], ["abc", "bcz"]]
visited = {"bcd", "bcz"}

Loop 2:
current_chain = ["abc", "bcd"]
queue = [["abc", "bcz"]]
last_word = "bcd"
last_two = "cd"
next_word = "cde"
queue = [["abc", "bcz"], ["abc", "bcd", "cde"]]
visited = {"bcd", "bcz", "cde"}

Loop 3:
current_chain = ["abc", "bcz"]
queue = [["abc", "bcd", "cde"]]
last_word = "bcz"
last_two = "cz"
next_word = NULL
queue = [["abc", "bcd", "cde"]]
visited = {"bcd", "bcz", "cde"}

Loop 4:
current_chain = ["abc", "bcd", "cde"]
queue = []
last_word = "cde"
last_two = "de"
next_word = "def"
new_chain = ["abc", "bcd", "cde", "def"]
queue = [["abc", "bcd", "cde", "def"]]
visited = {"bcd", "bcz", "cde","def"}

Loop 5:
current_chain = ["abc", "bcd", "cde", "def"]
queue = []
last_word = "def"

last_word == end_word nên trả về current_chain = ["abc", "bcd", "cde", "def"]
'''