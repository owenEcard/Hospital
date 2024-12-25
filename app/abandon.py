
# def handle_conversation():
#     context=about_ecard
#     print("welcome to the Ecard AI chatBox! Type '00' to quit")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             break

#         result = chain.invoke({"context":context,"question":user_input})
#         print("AI :",result)
#         context += f"\nUser:{user_input}\nAI{result}"

# if __name__ == "__main__":
#     handle_conversation()
