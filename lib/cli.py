from quiz_manager import QuizManager

class CLI:
    def __init__(self):
        self.manager = QuizManager()

    def main_menu(self):
        while True:
            print("\nQuiz Application")
            print("1. Manage Topics")
            print("2. Manage Quizzes")
            print("3. Take Quiz")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.manage_topics()
            elif choice == '2':
                self.manage_quizzes()
            elif choice == '3':
                self.take_quiz()
            elif choice == '4':
                print("Exiting application.")
                break
            else:
                print("Invalid choice, please try again.")

    def manage_topics(self):
        while True:
            print("\nManage Topics")
            print("1. Create Topic")
            print("2. Delete Topic")
            print("3. View All Topics")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter topic name: ")
                self.manager.create_topic(name)
                print(f"Topic '{name}' created.")
            elif choice == '2':
                topic_id = int(input("Enter topic ID to delete: "))
                self.manager.delete_topic(topic_id)
                print(f"Topic with ID {topic_id} deleted.")
            elif choice == '3':
                topics = self.manager.get_all_topics()
                for topic in topics:
                    print(f"ID: {topic.id}, Name: {topic.name}")
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def manage_quizzes(self):
        while True:
            print("\nManage Quizzes")
            print("1. Create Quiz")
            print("2. Delete Quiz")
            print("3. View All Quizzes")
            print("4. View Quizzes by Topic")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                question = input("Enter quiz question: ")
                options = input("Enter options (comma-separated): ")
                answer = input("Enter correct answer: ")
                topic_id = int(input("Enter topic ID: "))
                self.manager.create_quiz(question, options, answer, topic_id)
                print("Quiz created.")
            elif choice == '2':
                quiz_id = int(input("Enter quiz ID to delete: "))
                self.manager.delete_quiz(quiz_id)
                print(f"Quiz with ID {quiz_id} deleted.")
            elif choice == '3':
                quizzes = self.manager.get_all_quizzes()
                for quiz in quizzes:
                    print(f"ID: {quiz.id}, Question: {quiz.question}, Topic: {quiz.topic.name}")
            elif choice == '4':
                topic_id = int(input("Enter topic ID: "))
                quizzes = self.manager.get_quizzes_by_topic(topic_id)
                for quiz in quizzes:
                    print(f"ID: {quiz.id}, Question: {quiz.question}")
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def take_quiz(self):
        topic_id = int(input("Enter topic ID to take quiz: "))
        quizzes = self.manager.get_quizzes_by_topic(topic_id)
        score = 0

        for quiz in quizzes:
            print(f"Question: {quiz.question}")
            options = quiz.options.split(',')
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            answer = input("Enter the correct option number: ")

            if options[int(answer) - 1] == quiz.answer:
                score += 1

        print(f"You scored {score} out of {len(quizzes)}")

if __name__ == "__main__":
    CLI().main_menu()
