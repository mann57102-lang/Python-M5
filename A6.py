# Create a class
class find_pair:

    def findTwo(self, numbers, target_sum):
        # Create an empty dictionary
        positions = {}

        # Iterate through the tuple
        for index, number in enumerate(numbers):
            if target_sum - number in positions:
                return (positions[target_sum - number], index)

            positions[number] = index


# Take input from the user
search_value = int(
    input("Enter the target sum you want to search for: ")
)

print(
    "index1=%d, index2=%d"
    % find_pair().findTwo(
        (15, 25, 35, 45, 55, 65, 75),
        search_value
    )
)
