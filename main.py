import streamlit as st

# ================================
# 🎯 Full 20-Question C++ Quiz Data
# ================================
data = [
    {
        "question": """1. What will be the output of the following code?\n\n
        #include <iostream>\nusing namespace std;\n
        int main() 
        {\n    
        char c = 65;\n
        cout << c;\n    
        return 0;\n}""",
        "options": ["65", "A", "a", "Compilation Error"],
        "answer": "A",
        "explanation": "ASCII value 65 corresponds to 'A', so the output is 'A'."
    },
    {
        "question": "2. Which of the following declarations is invalid in C++?",
        "options": ["int num = 10.5;", "float x = 10;", "bool flag = 5;", 'char ch = "A";'],
        "answer": 'char ch = "A";',
        "explanation": 'Character literals must be in single quotes. "A" is a string literal, so use \'A\' instead.'
    },
    {
        "question": "3. What is the size of bool data type in C++ (on most modern compilers)?",
        "options": ["1 bit", "1 byte", "2 bytes", "Implementation dependent"],
        "answer": "1 byte",
        "explanation": "A bool is typically stored in 1 byte of memory, though only one bit is used logically."
    },
    {
        "question": """4. What will be the value of x after execution?\n\n
        int x = 10;\n
        {\n int x = 20;\n}\n
        x += 5;""",
        "options": ["10", "15", "20", "25"],
        "answer": "15",
        "explanation": "The inner x is destroyed after its scope ends. Outer x = 10, then x += 5 gives 15."
    },
    {
        "question": """5. What happens if you try to modify a const variable?\n\n
        #include <iostream>\nusing namespace std;\n
        int main() 
        {\n    const int x = 10;\n
        int *ptr = (int*)&x;\n 
        *ptr = 20;\n    
        cout << x << ' ' << *ptr;\n}""",
        "options": ["10 10", "10 20", "20 20", "Undefined Behavior"],
        "answer": "Undefined Behavior",
        "explanation": "Modifying a const variable through a pointer violates const correctness, leading to undefined behavior."
    },
    {
        "question": """6. What is the output of:\n\n
        #include <iostream>\nusing namespace std;\n
        int main() 
        {\n    int a = 5, b = 2;\n
        cout << a / b;\n
        return 0;\n}""",
        "options": ["2.5", "2", "2.0", "Error"],
        "answer": "2",
        "explanation": "Both operands are integers, so integer division is used. 5/2 = 2."
    },
    {
        "question": "7. Which of the following is used to define a constant in C++?",
        "options": ["#define PI 3.14", "const float PI = 3.14;", "Both A and B", "None"],
        "answer": "Both A and B",
        "explanation": "You can define constants using either #define or const keyword."
    },
    {
        "question": "8. Which of the following is not a valid C++ identifier?",
        "options": ["_value", "value1", "1value", "value_2"],
        "answer": "1value",
        "explanation": "Identifiers cannot start with a digit."
    },
    {
        "question": "9. Which operator cannot be overloaded in C++?",
        "options": ["++", "=", "::", "+"],
        "answer": "::",
        "explanation": "The scope resolution operator (::) cannot be overloaded."
    },
    {
        "question": "10. What is function overloading?",
        "options": [
            "Functions with same name but different parameters",
            "Functions with same name and same parameters",
            "Multiple functions calling each other",
            "Function inside a function"
        ],
        "answer": "Functions with same name but different parameters",
        "explanation": "Function overloading means same name but different parameter list."
    },
    {
        "question": """11. What will be the output?\n\n
        #include <iostream>\nusing namespace std;\n
        int main()
        {\n    int a = 5;\n
        cout << ++a << ' ' << a++;\n
        return 0;\n}""",
        "options": ["6 6", "5 5", "6 5", "5 6"],
        "answer": "6 6",
        "explanation": "++a increments before printing (6), then a++ prints 6 before incrementing."
    },
    {
        "question": "12. What is the default return type of a function in C++ if not specified?",
        "options": ["int", "void", "float", "None"],
        "answer": "int",
        "explanation": "By default, if return type is not specified, it is considered as int (in older C++, but now it's mandatory)."
    },
    {
        "question": """13. What will be printed?\n\n
        int x = 5;\n
        cout << (x == 5 ? 10 : 20);""",
        "options": ["5", "10", "20", "Error"],
        "answer": "10",
        "explanation": "Ternary operator returns 10 because x == 5 is true."
    },
    {
        "question": "14. What is the use of 'new' keyword in C++?",
        "options": [
            "To allocate memory dynamically",
            "To create objects only",
            "To allocate static memory",
            "To initialize variables"
        ],
        "answer": "To allocate memory dynamically",
        "explanation": "The 'new' keyword allocates memory on the heap dynamically."
    },
    {
        "question": """15. What will be the output of:\n\n
        int arr[5] = {1,2,3,4,5};\n
        cout << *(arr + 3);""",
        "options": ["3", "4", "2", "5"],
        "answer": "4",
        "explanation": "*(arr + 3) accesses the 4th element (index 3)."
    },
    {
        "question": "16. What will happen if you access out of bound index in an array?",
        "options": ["Compilation Error", "Runtime Error", "Undefined Behavior", "Zero value returned"],
        "answer": "Undefined Behavior",
        "explanation": "C++ does not perform bound checking, so accessing out of range causes undefined behavior."
    },
    {
        "question": "17. Which of the following is used to handle exceptions in C++?",
        "options": ["try-catch", "goto", "if-else", "error()"],
        "answer": "try-catch",
        "explanation": "C++ uses try-catch blocks to handle exceptions."
    },
    {
        "question": "18. Which of the following correctly declares a pointer?",
        "options": ["int ptr;", "int *ptr;", "int &ptr;", "int pointer;"],
        "answer": "int *ptr;",
        "explanation": "Pointer declaration syntax: type *pointerName;"
    },
    {
        "question": """19. What is the output?\n\n
        int x = 10;\n
        int &ref = x;\n
        ref = 20;\n
        cout << x;""",
        "options": ["10", "20", "0", "Error"],
        "answer": "20",
        "explanation": "ref is a reference to x, so modifying ref also changes x."
    },
    {
        "question": "20. Which header file is needed for using 'cout' and 'cin'?",
        "options": ["stdio.h", "iostream", "conio.h", "stdlib.h"],
        "answer": "iostream",
        "explanation": "'cout' and 'cin' are part of the iostream library."
    }
]

# ================================
# ⚙️ Session State Initialization
# ================================
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None

# ================================
# 🔁 Reset Function
# ================================
def reset_quiz():
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.selected_answer = None

def next_question():
    st.session_state.current_q += 1
    st.session_state.submitted = False
    st.session_state.selected_answer = None

# ================================
# 🧠 Quiz Logic
# ================================
st.title("💡 Interactive C++ Quiz")
st.write("Test your C++ knowledge! Answer each question and learn from detailed explanations.")
st.divider()

if st.session_state.current_q < len(data):
    q = data[st.session_state.current_q]
    
    # Progress indicator
    progress = (st.session_state.current_q) / len(data)
    st.progress(progress)
    st.write(f"**Question {st.session_state.current_q + 1} of {len(data)}** | Score: {st.session_state.score}/{st.session_state.current_q}")
    
    st.markdown("---")
    st.markdown(f"### {q['question']}")
    
    # Display options
    if not st.session_state.submitted:
        selected = st.radio(
            "Select your answer:",
            q["options"],
            key=f"q{st.session_state.current_q}",
            index=None
        )
        
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button("✓ Submit Answer", type="primary", disabled=(selected is None)):
                st.session_state.selected_answer = selected
                st.session_state.submitted = True
                st.session_state.answers[st.session_state.current_q] = selected
                
                if selected == q["answer"]:
                    st.session_state.score += 1
                st.rerun()
    else:
        # Show result after submission
        selected = st.session_state.selected_answer
        correct = q["answer"]
        
        # Display all options with visual feedback
        for option in q["options"]:
            if option == correct:
                st.success(f"✅ {option} (Correct Answer)")
            elif option == selected and option != correct:
                st.error(f"❌ {option} (Your Answer)")
            else:
                st.write(f"⚪ {option}")
        
        st.markdown("---")
        
        # Show result
        if selected == correct:
            st.success("🎉 **Correct!** Well done!")
        else:
            st.error(f"❌ **Incorrect!** The correct answer is: **{correct}**")
        
        # Show explanation
        st.info(f"**💡 Explanation:** {q['explanation']}")
        
        st.markdown("---")
        
        # Next button
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.session_state.current_q < len(data) - 1:
                if st.button("Next Question →", type="primary"):
                    next_question()
                    st.rerun()
            else:
                if st.button("View Results →", type="primary"):
                    next_question()
                    st.rerun()

else:
    # Quiz completed - show results
    st.success("🎉 **Quiz Completed!**")
    st.markdown("---")
    
    total = len(data)
    score = st.session_state.score
    percentage = (score / total) * 100
    
    # Display score with visual feedback
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Your Score", f"{score}/{total}")
    with col2:
        st.metric("Percentage", f"{percentage:.1f}%")
    with col3:
        if percentage >= 80:
            grade = "A - Excellent! 🌟"
        elif percentage >= 60:
            grade = "B - Good Job! 👍"
        elif percentage >= 40:
            grade = "C - Keep Learning! 📚"
        else:
            grade = "D - Practice More! 💪"
        st.metric("Grade", grade)
    
    st.progress(score / total)
    
    # Performance message
    st.markdown("---")
    if percentage == 100:
        st.balloons()
        st.success("🏆 **Perfect Score!** You're a C++ master!")
    elif percentage >= 80:
        st.success("🌟 **Excellent work!** You have a strong grasp of C++ concepts.")
    elif percentage >= 60:
        st.info("👍 **Good job!** Keep practicing to improve further.")
    elif percentage >= 40:
        st.warning("📚 **Keep learning!** Review the concepts and try again.")
    else:
        st.warning("💪 **Don't give up!** Practice makes perfect. Review the material and retry.")
    
    # Show detailed results
    st.markdown("---")
    st.subheader("📊 Detailed Results")
    
    for i, q in enumerate(data):
        user_answer = st.session_state.answers.get(i, "Not answered")
        correct_answer = q["answer"]
        is_correct = user_answer == correct_answer
        
        with st.expander(f"Question {i+1}: {'✅' if is_correct else '❌'}"):
            st.markdown(f"**{q['question']}**")
            st.write(f"**Your answer:** {user_answer}")
            st.write(f"**Correct answer:** {correct_answer}")
            st.info(f"**Explanation:** {q['explanation']}")
    
    # Restart button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("🔄 Restart Quiz", type="primary"):
            reset_quiz()
            st.rerun()
