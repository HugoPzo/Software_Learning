# +++++++++Condition Statements+++++++++
# 7


age = int(input("How old are you?: "))

# The order of the conditions matters


# In this case, if the condition 'age == 100' is below condition 'age >= 18'
# the condition of 'age 100' never is fulfilled

if age == 100:
    print("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a young guy")