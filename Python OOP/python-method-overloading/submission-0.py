class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, *args: str) -> str:
        if len(args) == 1:
            first_arg = args[0]
            upper_case = first_arg.upper()
            return(upper_case)
        elif len(args) == 2:
            concatenated = args[0] + args[1]
            return(concatenated)
        else:
            return("Number of Arguments entered not acceptable")




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
