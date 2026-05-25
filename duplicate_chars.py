sample = "Selenium is open source"

store_dict = {}

# Count characters
for ch in sample:
    if ch != ' ':   # Ignore spaces
        store_dict[ch] = store_dict.get(ch, 0) + 1

# Print duplicate characters
for key, value in store_dict.items():
    if value > 1:
        print(f"Character: {key} is displayed: {value} times")