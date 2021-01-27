# Read
# Method 1
file = open('/Users/Abhijeet/Desktop/my_file.txt', 'r') # Absolute paths: wrt root
file = open('../../../Desktop/my_file.txt', 'r') # Relative paths: wrt pwd
contents = file.read()
print(contents)
file.close()
# # Method 2
with open('my_file.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Write
with open('my_file.txt','w') as file:
    file.write('Hello Moto')

# Append
with open('my_file.txt','a') as file:
    file.write('\nMotorolla')