import streamlit as st

# ================================
# 🎯 C++ Quiz Data - Easy to Moderate
# Topics: Variables, Data Types, Const, Arithmetic Operators, Type Conversion, If Statements
# ================================
data = [
    # Variables and Basic Data Types
    {
        "question": "1. Which of the following is a valid variable name in C++?",
        "code": None,
        "options": ["int", "my_age", "2nd_value", "my-name"],
        "answer": "my_age",
        "explanation": "Variable names can contain letters, digits, and underscores, but must start with a letter or underscore. 'int' is a keyword, '2nd_value' starts with a digit, and 'my-name' contains a hyphen."
    },
    {
        "question": "2. What will be the output of this code?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int x = 10;
    cout << x;
    return 0;
}""",
        "options": ["x", "10", "0", "Error"],
        "answer": "10",
        "explanation": "The variable x is assigned the value 10, and cout prints the value stored in x, which is 10."
    },
    {
        "question": "3. What is the correct way to declare a floating-point variable in C++?",
        "code": None,
        "options": ["float x = 5.5;", "float x = 5;", "double x = 3.14;", "All of the above"],
        "answer": "All of the above",
        "explanation": "All three declarations are valid. float and double can store decimal numbers, and integers can be assigned to float/double (they will be converted to floating-point)."
    },
    {
        "question": "4. What will be printed?",
        "code": """#include <iostream>
using namespace std;

int main() {
    bool flag = true;
    cout << flag;
    return 0;
}""",
        "options": ["true", "false", "1", "0"],
        "answer": "1",
        "explanation": "When a boolean is printed using cout, true is displayed as 1 and false as 0."
    },
    
    # Const
    {
        "question": "5. What happens when you try to modify a const variable?",
        "code": """const int x = 10;
x = 20;""",
        "options": ["The code runs successfully", "Compilation error", "Runtime error", "x becomes 20"],
        "answer": "Compilation error",
        "explanation": "const variables cannot be modified after initialization. Attempting to change them causes a compilation error."
    },
    {
        "question": "6. Which statement correctly declares a constant?",
        "code": None,
        "options": ["const PI = 3.14;", "const float PI = 3.14;", "float const PI;", "constant float PI = 3.14;"],
        "answer": "const float PI = 3.14;",
        "explanation": "Constants must be declared with both the const keyword and a data type, and must be initialized at declaration."
    },
    {
        "question": "7. What will be the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    const int x = 5;
    const int y = x + 10;
    cout << y;
    return 0;
}""",
        "options": ["5", "10", "15", "Error"],
        "answer": "15",
        "explanation": "const variables can be initialized using expressions involving other const or regular variables. y = 5 + 10 = 15."
    },
    
    # Arithmetic Operators
    {
        "question": "8. What is the result of 17 % 5?",
        "code": None,
        "options": ["3", "2", "3.4", "0"],
        "answer": "2",
        "explanation": "The modulus operator (%) returns the remainder of division. 17 divided by 5 is 3 with a remainder of 2."
    },
    {
        "question": "9. What will be the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;
    cout << a / b;
    return 0;
}""",
        "options": ["3.333", "3", "3.0", "4"],
        "answer": "3",
        "explanation": "When both operands are integers, integer division is performed. 10/3 = 3 (decimal part is discarded)."
    },
    {
        "question": "10. What is the value of x after this code?",
        "code": """int x = 5;
x = x + 3;
x = x * 2;""",
        "options": ["8", "10", "16", "13"],
        "answer": "16",
        "explanation": "Step by step: x = 5, then x = 5 + 3 = 8, then x = 8 * 2 = 16."
    },
    {
        "question": "11. What will be printed?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int b = ++a;
    cout << b;
    return 0;
}""",
        "options": ["10", "11", "9", "Error"],
        "answer": "11",
        "explanation": "++a is prefix increment, which increments a first (a becomes 11), then assigns to b. So b = 11."
    },
    {
        "question": "12. What is the difference between a++ and ++a?",
        "code": None,
        "options": [
            "a++ increments after use, ++a increments before use",
            "They are exactly the same",
            "a++ is faster than ++a",
            "++a can only be used with integers"
        ],
        "answer": "a++ increments after use, ++a increments before use",
        "explanation": "++a (prefix) increments the value first, then uses it. a++ (postfix) uses the current value, then increments."
    },
    
    # Type Conversion
    {
        "question": "13. What will be the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int a = 5;
    float b = 2.5;
    cout << a + b;
    return 0;
}""",
        "options": ["7", "7.5", "7.0", "Error"],
        "answer": "7.5",
        "explanation": "When an int and float are added, the int is automatically converted to float. 5 + 2.5 = 7.5."
    },
    {
        "question": "14. What is the value of result?",
        "code": """int a = 10;
int b = 4;
float result = a / b;""",
        "options": ["2.5", "2.0", "2", "3"],
        "answer": "2.0",
        "explanation": "a/b is integer division (10/4 = 2), then the integer result 2 is converted to float 2.0 when assigned to result."
    },
    {
        "question": "15. How do you correctly convert int to float during division?",
        "code": None,
        "options": [
            "float result = a / b;",
            "float result = (float)a / b;",
            "float result = float(a / b);",
            "float result = a // b;"
        ],
        "answer": "float result = (float)a / b;",
        "explanation": "Casting at least one operand to float before division ensures floating-point division. (float)a / b or a / (float)b works."
    },
    {
        "question": "16. What will be printed?",
        "code": """#include <iostream>
using namespace std;

int main() {
    double x = 9.8;
    int y = x;
    cout << y;
    return 0;
}""",
        "options": ["9.8", "9", "10", "Error"],
        "answer": "9",
        "explanation": "When assigning a double to an int, the decimal part is truncated (not rounded). 9.8 becomes 9."
    },
    
    # If Statements
    {
        "question": "17. What will be the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int x = 15;
    if (x > 10) {
        cout << "Large";
    }
    return 0;
}""",
        "options": ["Large", "10", "15", "Nothing"],
        "answer": "Large",
        "explanation": "The condition x > 10 is true (15 > 10), so the code inside the if block executes and prints 'Large'."
    },
    {
        "question": "18. What will be printed?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int age = 16;
    if (age >= 18) {
        cout << "Adult";
    } else {
        cout << "Minor";
    }
    return 0;
}""",
        "options": ["Adult", "Minor", "16", "Nothing"],
        "answer": "Minor",
        "explanation": "Since age (16) is not >= 18, the condition is false, so the else block executes and prints 'Minor'."
    },
    {
        "question": "19. What is the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int num = 10;
    if (num > 5 && num < 15) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}""",
        "options": ["Yes", "No", "10", "Error"],
        "answer": "Yes",
        "explanation": "Both conditions are true: num > 5 (10 > 5) AND num < 15 (10 < 15), so 'Yes' is printed."
    },
    {
        "question": "20. What will be the output?",
        "code": """#include <iostream>
using namespace std;

int main() {
    int score = 85;
    if (score >= 90) {
        cout << "A";
    } else if (score >= 80) {
        cout << "B";
    } else {
        cout << "C";
    }
    return 0;
}""",
        "options": ["A", "B", "C", "85"],
        "answer": "B",
        "explanation": "score (85) is not >= 90, so the first condition fails. Then score >= 80 is true, so 'B' is printed."
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
st.title("💡 C++ Fundamentals Quiz")
st.write("📚 **Topics Covered:** Variables, Data Types, Const, Arithmetic Operators, Type Conversion, If Statements")
st.divider()

if st.session_state.current_q < len(data):
    q = data[st.session_state.current_q]
    
    # Progress indicator
    progress = (st.session_state.current_q) / len(data)
    st.progress(progress)
    st.write(f"**Question {st.session_state.current_q + 1} of {len(data)}** | Current Score: {st.session_state.score}/{st.session_state.current_q if st.session_state.current_q > 0 else 1}")
    
    st.markdown("---")
    
    # Display question
    st.markdown(f"### {q['question']}")
    
    # Display code snippet if present
    if q['code']:
        st.code(q['code'], language='cpp')
    
    # Display options
    if not st.session_state.submitted:
        selected = st.radio(
            "**Select your answer:**",
            q["options"],
            key=f"q{st.session_state.current_q}",
            index=None
        )
        
        st.markdown("")  # Add spacing
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
        
        st.markdown("#### Your Answer:")
        # Display all options with visual feedback
        for option in q["options"]:
            if option == correct:
                st.success(f"✅ {option} **(Correct Answer)**")
            elif option == selected and option != correct:
                st.error(f"❌ {option} **(Your Answer)**")
            else:
                st.write(f"⚪ {option}")
        
        st.markdown("---")
        
        # Show result
        if selected == correct:
            st.success("### 🎉 Correct! Well done!")
        else:
            st.error(f"### ❌ Incorrect!")
            st.write(f"**The correct answer is:** {correct}")
        
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
        if percentage >= 90:
            grade = "A - Outstanding! 🏆"
        elif percentage >= 80:
            grade = "B - Great! 🌟"
        elif percentage >= 70:
            grade = "C - Good! 👍"
        elif percentage >= 60:
            grade = "D - Fair 📚"
        else:
            grade = "F - Keep Practicing 💪"
        st.metric("Grade", grade)
    
    st.progress(score / total)
    
    # Performance message
    st.markdown("---")
    if percentage == 100:
        st.balloons()
        st.success("### 🏆 Perfect Score! You're a C++ Master!")
        st.write("You've demonstrated excellent understanding of C++ fundamentals!")
    elif percentage >= 80:
        st.success("### 🌟 Excellent Work!")
        st.write("You have a strong grasp of C++ concepts. Keep up the great work!")
    elif percentage >= 60:
        st.info("### 👍 Good Job!")
        st.write("You're on the right track. Review the questions you missed and keep practicing!")
    else:
        st.warning("### 💪 Keep Learning!")
        st.write("Don't give up! Review the material and try again. Practice makes perfect!")
    
    # Topic-wise breakdown
    st.markdown("---")
    st.subheader("📊 Topic Coverage")
    st.write("""
    - **Questions 1-4:** Variables and Basic Data Types
    - **Questions 5-7:** Const Variables
    - **Questions 8-12:** Arithmetic Operators
    - **Questions 13-16:** Type Conversion
    - **Questions 17-20:** If Statements
    """)
    
    # Show detailed results
    st.markdown("---")
    st.subheader("📋 Detailed Results")
    
    for i, q in enumerate(data):
        user_answer = st.session_state.answers.get(i, "Not answered")
        correct_answer = q["answer"]
        is_correct = user_answer == correct_answer
        
        with st.expander(f"Question {i+1}: {'✅ Correct' if is_correct else '❌ Incorrect'}"):
            st.markdown(f"**{q['question']}**")
            if q['code']:
                st.code(q['code'], language='cpp')
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
    with col2:
        st.write("**Good luck on your next attempt!**")
