import streamlit as st

st.title("FLAMES Game")

a = list(st.text_input("Enter first name").lower())
b = list(st.text_input("Enter second name").lower())

for i in a.copy():
    if i in b:
        a.remove(i)
        b.remove(i)

n = len(a + b)
s = "flames"

while len(s) != 1:
    i = n % len(s) - 1
    if i == -1:
        s = s[:len(s) - 1]
    else:
        s = s[i + 1:] + s[:i]

d = {
    'f': 'Friends',
    'l': 'Love',
    'a': 'Affection',
    'm': 'Marriage',
    'e': 'Engaged',
    's': 'Siblings'
}

if st.button("Get Result"):
    st.success(d[s])
