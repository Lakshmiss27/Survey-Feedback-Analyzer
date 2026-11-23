

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):

    name = input("Enter your name: ")

    feedback = input("Enter your feedback: ")

    rating = int(input("Enter your rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)

    feedback_data['Name'].append(name)

    feedback_data['Feedback'].append(feedback)

    feedback_data['Rating'].append(rating)


while rating < 1 or rating > 5:
    print("Invalid rating. Please enter between 1 and 5.")
    


for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    feedback = feedback.lower()

    feedback = feedback.replace('.', '')
    feedback = feedback.replace(',', '')
    feedback = feedback.replace('!', '')
    feedback = feedback.replace('?', '')

    feedback = ' '.join(feedback.split())

    feedback_data['Feedback'][i] = feedback


def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        if word.lower() in feedback.lower().split():

            count = count + 1

    return count


print("Feedbacks containing good:",
      count_word_in_feedbacks("good"))

print("Feedbacks containing poor:",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing excellent:",
      count_word_in_feedbacks("excellent"))

print("\nFinal Cleaned Feedback Data:")

print(feedback_data)

total_rating = sum(feedback_data['Rating'])

total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("Average Rating:", average_rating)




unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        unique_words.add(word)

print("Unique Words:")
print(sorted(unique_words))

sorted_feedbacks = sorted(
    zip(
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[2],
    reverse=True
)

print("\nFeedbacks Sorted by Rating:")

for item in sorted_feedbacks:

    print(item)

