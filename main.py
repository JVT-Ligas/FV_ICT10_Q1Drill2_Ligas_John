from pyscript import document, display

# This function is triggered when the submit button is clicked
def on_click(event):
    # Get values from the input fields in the HTML document
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Info sheet using multiple f-strings concatenated for multiline formatting
    info = (
        # Title with newline
        f"Information Sheet\n"           
        
        # Separator line
        f"-----------------\n"           
        
        # Name with tab and newline
        f"Name:\t{name}\n"               
        
        # Age with tab and newline
        f"Age:\t{age}\n"                 
        
        # School with tab and two newlines
        f"School:\t{school}\n\n"         
        
        # Notes section
        f"Notes:\n"                      
        
        # Detailed information using embedded f-strings
        f"{name} is currently {age} and studies at {school}. "
        
        # Final note
        f"Information was gathered through the inputted fields above."
    )
    
    # Display the formatted information in the HTML element
    display(info, target="string")

