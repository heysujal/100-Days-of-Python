import requests


class Settings:

    def __init__(self):

        self.amount = input("Enter number of questions(press ENTER for default: 10): ") or "10"
        self.category = input("Enter category id (press ENTER for default: all)\n"
                              "1  : General Knowledge\n"
                              "2  : Entertainment: Books\n"
                              "3  : Entertainment: Film\n"
                              "4  : Entertainment: Music\n"
                              "5  : Entertainment: Musicals and festival\n"
                              "6  : Entertainment: Television\n"
                              "7  : Entertainment: Video Games\n"
                              "8  : Entertainment: Board Games\n"
                              "9  : Science and Nature\n"
                              "10 : Science: Computer\n"
                              "11 : Science: Mathematics\n"
                              "12 : Mythology\n"
                              "13 : Sports\n"
                              "14 : Geography\n"
                              "15 : History\n"
                              "16 : Politics\n"
                              "17 : Art\n"
                              "18 : Celebrities\n"
                              "19 : Animals\n") or ""
        if not self.category == "":
            self.category = str(int(self.category) + 8)
        self.difficulty = input("Select difficulty (easy/medium/hard): ") or ""
        self.question_list = []

    def get_questions(self):
        url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.category}&" \
              f"difficulty={self.difficulty}&type=boolean"
        # print(url)
        x = requests.get(url)
        response = x.json()
        # print(response)
        if not response["results"]:
            print("Sorry! 😔. There are no questions available for these settings!")

        self.question_list = response["results"]

        # print(self.question_list)
