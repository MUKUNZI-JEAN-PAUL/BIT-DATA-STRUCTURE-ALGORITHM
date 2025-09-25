#stack insert
stack1 = []
stack1.append("Enter Code")
stack1.append("PIN")
stack1.append("Confirm")

print("Stack (bottom -> top):", stack1)

popped = stack1.pop()   # undo 1
print("Popped (undo):", popped)
print("Stack now (bottom -> top):", stack1)
print("Top now:", stack1[-1])
