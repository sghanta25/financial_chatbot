def financial_chatbot(user_query):
    if user_query == "What is the total revenue of Apple in 2024?":
        return "The total revenue is $1,431,468."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by $36,575 over the last year."
    elif user_query == "What was the revenue growth in the last fiscal year?":
        return "The revenue growth in the last fiscal year was 6.52 %."
    else:
        return "I'm not sure how to answer that. Can you try a different question?"

if __name__ == "__main__":
    while True:
        user_input = input("Ask a financial question: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = financial_chatbot(user_input)
        print(response)
