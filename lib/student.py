class Student:
    # Method to print a greeting message
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    # Method to raise hand
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    # Overriding the hello method
    def hello(self):
        # Call the hello method from the parent class
        super().hello()
        # Augment with chatty behavior
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")
    
    # Overriding the raise_hand method
    def raise_hand(self):
        # Call the raise_hand method from the parent class 10 times
        for _ in range(10):
            super().raise_hand()

# Testing the functionality
if __name__ == "__main__":
    # Create an instance of Student
    student = Student()
    print("Student says:")
    student.hello()
    student.raise_hand()
    
    print("\nChattyStudent says:")
    # Create an instance of ChattyStudent
    chatty_student = ChattyStudent()
    chatty_student.hello()
    chatty_student.raise_hand()            
