# This file can contain various utility functions.

# Example: Function to truncate a string
def truncate_string(text, max_length):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text