import csv

from flask import Flask, flash, render_template, redirect, url_for, session, request

app = Flask(__name__)

i = 0

@app.route("/games/<int:i>", methods=["GET", "POST"])
def games(i):
    # return redirect("/games/0.html")
    with open("static/questions.csv") as data_csv:
        requested_question = None
        question_data = csv.DictReader(data_csv)
        data = []
        for row in question_data:
            data.append(row)
        count = len(data)
        number = data[i]['id']
        question_text = data[i]['Question']
        answer_1 = data[i]['Answer 1']
        answer_2 = data[i]['Answer 2']
        answer_3 = data[i]['Answer 3']
        correct_answer = data[i]['Correct Answer']
        image_1 = data[i]['Image 1']
        image_2 = data[i]['Image 2']
        image_3 = data[i]['Image 3']
        sound_1 = data[i]['Sound 1']
        sound_2 = data[i]['Sound 2']
        sound_3 = data[i]['Sound 3']
        question_sound = data[i]['Question sound']

        i += 1

        # Prevent user going past the last question
        if i == count:
            return render_template("games.html", question_text=question_text, answer_1=answer_1, answer_2=answer_2,
                                answer_3=answer_3, correct_answer=correct_answer, requested_question=number, i=(count-1),
                                image_1=image_1, image_2=image_2, image_3=image_3, sound_1=sound_1, sound_2=sound_2, sound_3=sound_3, question_sound=question_sound)
        # Prevent user going past the first question
        elif i <= 1:
            return render_template("games.html", question_text=question_text, answer_1=answer_1, answer_2=answer_2,
                                answer_3=answer_3, correct_answer=correct_answer, requested_question=number, i=1,
                                image_1=image_1, image_2=image_2, image_3=image_3, sound_1=sound_1, sound_2=sound_2, sound_3=sound_3, question_sound=question_sound)

        else:
            return render_template("games.html", question_text=question_text, answer_1=answer_1, answer_2=answer_2,
                                answer_3=answer_3, correct_answer=correct_answer, requested_question=number, i=i, count=count,
                                image_1=image_1, image_2=image_2, image_3=image_3, sound_1=sound_1, sound_2=sound_2, sound_3=sound_3, question_sound=question_sound)

if __name__ == "__main__":
    app.run(debug=True)