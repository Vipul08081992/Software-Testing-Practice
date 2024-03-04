
def sort_list(input_list,desc):
    try:
        sorted_list = sorted(input_list,reverse=desc)
        return sorted_list
    except Exception as e:
        print(f"An error occurred: {str(e)}")

