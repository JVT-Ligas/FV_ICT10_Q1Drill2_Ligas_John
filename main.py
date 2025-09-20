from pyscript import document, display

# This function is triggered when the submit button is clicked
def on_click(event):
    # Get values from the input fields in the HTML document
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Clear previous message to avoid duplicates
    document.getElementById("string").textContent = ""

    # Info sheet using multiple f-strings concatenated for multiline formatting
    info = (
        f"Information Sheet\n"
        f"-----------------\n"
        f"Name:\t{name}\n"
        f"Age:\t{age}\n"
        f"School:\t{school}\n\n"
        f"Notes:\n"
        f"{name} is currently {age} and studies at {school}. "
        f"Information was gathered through the inputted fields above."
    )
    
    # Display the formatted information in the HTML element
    display(info, target="string")

