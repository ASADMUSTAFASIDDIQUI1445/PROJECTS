import streamlit as st
import re


def check_password_strength(password):
    messages = []
    score = 0

    # Length check
    if len(password) >= 10:
        score += 1
    else:
        messages.append(("error", "Password should be at least 10 characters long."))

    # Uppercase and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        messages.append(("error", " Include both uppercase and lowercase letters."))

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        messages.append(("error", " Add at least one number (0-9)."))

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        messages.append(("error", " Include at least one special character (!@#$%^&*)."))

    # Final assessment
    if score == 4:
        messages.append(("success", " Strong Password!"))
    elif score == 3:
        messages.append(("warning", " Moderate Password - Consider adding more security features."))
    else:
        messages.append(("error", " Weak Password - Improve it using the suggestions above."))

    return messages


# Streamlit UI
st.title(" Password Strength Checker & Generator")
password = st.text_input("Enter password:")
if st.button("Check Strength"):
    feedback = check_password_strength(password)
    for msg_type, msg in feedback:
        if msg_type == "error":
            st.error(msg)
        elif msg_type == "warning":
            st.warning(msg)
        elif msg_type == "success":
            st.success(msg)