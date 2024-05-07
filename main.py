import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import random

# <==== Code starts here ====>

courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)

    return recommended_course_names




st.markdown("<h1 style='text-align: center; color: yellow;'>NIE Institute Of Technology, Mysuru</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: yellow;'><hr></h6>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ffff66;'>Empowering Education with AI</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>An application created towards fulfillment of final year project by : <br><br>Abhigyan Aman &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[4NN20CS001]<br>Aditya &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[4NN20CS005]<br>Ravala Pallavika &nbsp&nbsp&nbsp&nbsp[4NN20CS042]<br>Sai Charita &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[4NN20CS043]</h2>", unsafe_allow_html=True)


def course_recommendation():
    st.markdown("<h2 style='text-align: center; color: #ffff80;'>Selective Course Recommendation System</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #ffffb3;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)

    course_list = courses_list['course_name'].values
    selected_course = st.selectbox(
        "Type or select a course you like :",
        courses_list
    )

    if st.button('Show Recommended Courses'):
        st.write("Recommended Courses based on your interests are :")
        recommended_course_names = recommend(selected_course)
        st.text(recommended_course_names[0])
        st.text(recommended_course_names[1])
        st.text(recommended_course_names[2])
        st.text(recommended_course_names[3])
        st.text(recommended_course_names[4])
        st.text(recommended_course_names[5])
        st.text(" ")
        st.markdown("<h6 style='text-align: center; color: red;'>&copyA combined final year project by Abhigyan Aman and team.</h6>", unsafe_allow_html=True)

# <==== Code ends here ====>


easy_algebra_questions = [
    "What is 2 + 2?",
    "Solve for x: 3x = 9",
    "What is the value of y when x = 5 in the equation y = 2x + 3?",
    "If 4x + 7 = 19, what is the value of x?",
    "Factorize the expression: x^2 + 4x + 4",
    "If y = 3x + 2 and x = 4, what is the value of y?",
    "What is the result of 5x - 3y if x = 2 and y = 4?",
    "If x + 3 = 9, what is the value of x?",
    "Simplify the expression: 2(3x - 4)",
    "What is the value of z in the equation 2z - 8 = 10?",
    "What is 2 + 2?",
    "Solve for x: 3x = 9",
    "What is the value of y when x = 5 in the equation y = 2x + 3?",
    "If 4x + 7 = 19, what is the value of x?",
    "Factorize the expression: x^2 + 4x + 4",
    "If y = 3x + 2 and x = 4, what is the value of y?",
    "What is the result of 5x - 3y if x = 2 and y = 4?",
    "If x + 3 = 9, what is the value of x?",
    "Simplify the expression: 2(3x - 4)",
    "What is the value of z in the equation 2z - 8 = 10?",
    "What is 3 times 5?",
    "Solve for x: x + 6 = 10",
    "What is the value of y when x = 2 in the equation y = x + 3?",
    "If 3x + 4 = 16, what is the value of x?",
    "Factorize the expression: x^2 - 9",
    "If y = 2x - 1 and x = 3, what is the value of y?",
    "What is the result of 4x + 7y if x = 3 and y = 2?",
    "If 2x - 5 = 7, what is the value of x?",
    "Simplify the expression: 3(2x - 5)",
    "What is the value of z in the equation z + 2 = 8?",
    "What is 4 plus 3?",
    "Solve for x: 2x = 10",
    "What is the value of y when x = 3 in the equation y = 5x - 2?",
    "If 5x - 3 = 22, what is the value of x?",
    "Factorize the expression: x^2 + 6x + 9",
    "If y = x - 2 and x = 4, what is the value of y?",
    "What is the result of 3x - 2y if x = 4 and y = 3?",
    "If x + 5 = 11, what is the value of x?",
    "Simplify the expression: 2(4x - 3)",
    "What is the value of z in the equation 3z - 7 = 8?",
    "What is 6 divided by 2?",
    "Solve for x: 4x = 20",
    "What is the value of y when x = 4 in the equation y = 3x + 1?",
    "If 2x + 1 = 9, what is the value of x?",
    "Factorize the expression: x^2 - 4",
    "If y = 3x + 2 and x = 2, what is the value of y?",
    "What is the result of 5x - 4y if x = 3 and y = 2?",
    "If x + 2 = 8, what is the value of x?",
    "Simplify the expression: 3(3x - 2)",
    "What is the value of z in the equation 4z - 6 = 10?"
]

medium_algebra_questions = [
    "What is the value of x in the equation 2x + 5 = 15?",
    "Solve for y: 3y - 7 = 17",
    "If f(x) = 3x^2 + 5x - 2, what is f(2)?",
    "Simplify the expression: (2x^2 - 3x + 4) + (3x^2 + 2x - 1)",
    "Find the slope of the line passing through the points (2, 3) and (5, 9)",
    "What is the value of y in the equation 2x + 4y = 12, if x = 3?",
    "Solve for x: 2(x - 4) = 10",
    "If g(x) = 4x - 3, what is g(5)?",
    "Factorize the expression: 2x^2 + 5x - 3",
    "Simplify the expression: 3(x + 2) + 2(x - 3)",
    "What is the value of x in the equation 2x + 5 = 15?",
    "Solve for y: 3y - 7 = 17",
    "If f(x) = 3x^2 + 5x - 2, what is f(2)?",
    "Simplify the expression: (2x^2 - 3x + 4) + (3x^2 + 2x - 1)",
    "Find the slope of the line passing through the points (2, 3) and (5, 9)",
    "What is the value of y in the equation 2x + 4y = 12, if x = 3?",
    "Solve for x: 2(x - 4) = 10",
    "If g(x) = 4x - 3, what is g(5)?",
    "Factorize the expression: 2x^2 + 5x - 3",
    "Simplify the expression: 3(x + 2) + 2(x - 3)",
    "What is the value of x in the equation 3x + 2y = 10 and y = 2?",
    "Solve for x: 4x - 7 = 11",
    "If h(x) = x^2 + 4x + 3, what is h(-2)?",
    "What is the solution to the equation 2(x - 3) = 4x?",
    "Find the y-intercept of the line with equation y = 2x - 5",
    "Determine the slope of the line passing through the points (-1, 4) and (3, -2)",
    "What is the value of y in the equation 3y - 2x = 12, if x = 4?",
    "Solve for x: 5x - 3 = 22",
    "If p(x) = 2x^3 - 5x^2 + 3x - 7, what is p(3)?",
    "What is the result of 2(x + 3) - 3(x - 1) if x = 2?",
    "What is the value of x in the equation |2x - 3| = 5?",
    "Solve for y: 2x + 3y = 15 and x = 3",
    "If f(x) = 2x^2 + 3x - 4, what is f(-2)?",
    "What is the result of 3(2x - 5) - 2(3x + 1) if x = 4?",
    "Find the slope of the line parallel to y = 4x - 3",
    "What is the value of y in the equation 4y - 3x = 20, if x = 5?",
    "Solve for x: 3(x + 2) = 5(2x - 1)",
    "If g(x) = 3x^2 - 2x + 1, what is g(3)?",
    "What is the y-coordinate of the point where the line y = 2x + 1 intersects the x-axis?",
    "Find the x-intercept of the line with equation y = -3x + 6",
    "Determine the slope of the line passing through the points (-2, 5) and (3, -1)",
    "What is the value of y in the equation 5x + 2y = 16, if x = 3?",
    "Solve for x: |3x - 5| = 7",
    "If h(x) = x^2 - 4x + 3, what is h(2)?",
    "What is the result of 4x + 2y if x = 3 and y = 5?",
    "Find the slope of the line perpendicular to y = -2x + 4",
    "What is the value of y in the equation 2y - 3x = 10, if x = 2?",
    "Solve for x: 2(x - 4) = 6",
    "If p(x) = 4x^2 - 3x + 2, what is p(-1)?",
    "What is the y-intercept of the line with equation y = 3x + 2?"
    
]

hard_algebra_questions = [
    "Solve for x: 5x^2 - 3x + 2 = 0",
    "Find the roots of the equation 2x^2 - 7x + 3 = 0",
    "What is the equation of the line perpendicular to y = 3x - 2 passing through the point (4, 5)?",
    "Determine the distance between the points (2, 5) and (-3, -1)",
    "Find the value of y: 2y - 7 = 11",
    "If h(x) = x^2 + 4x + 3, what is h(-2)?",
    "Solve for x: |2x - 5| = 11",
    "What is the y-intercept of the line with equation y = -2x + 4?",
    "If p(x) = 2x^3 - 5x^2 + 3x - 7, what is p(3)?",
    "What is the solution set of the equation |3x - 2| = 4?",
    "Find the solution set of the inequality: 3x^2 - 5x < 2",
    "What is the value of x in the equation 2^(x-1) + 2^(x+1) = 40?",
    "Solve the system of equations: {2x + 3y = 5, x - y = 1}",
    "Factorize the expression: x^3 + 8y^3",
    "Find the value of x: log(x) + log(x-2) = 1",
    "What is the domain of the function f(x) = sqrt(4 - x^2)?",
    "Simplify the expression: (sin(x) + cos(x))^2 - sin^2(x) - cos^2(x)",
    "Solve for x: e^(2x) - 5e^x + 6 = 0",
    "Find the inverse function of f(x) = 3x^2 + 2x + 1",
    "Determine the discriminant of the quadratic equation: 2x^2 + 5x - 3 = 0",
    "What are the real roots of the equation: x^3 - 6x^2 + 11x - 6 = 0?",
    "If f(x) = x^4 - 3x^3 + 2x^2 + 5x - 6, what are the critical points of f(x)?",
    "Solve for x: sin(2x) + cos(x) = 0",
    "Find the equation of the tangent line to the curve y = x^3 - 2x^2 + x + 1 at the point (1, 1)",
    "What is the range of the function g(x) = 2x^2 - 3x + 1?",
    "Find the roots of the equation 5x^3 - 3x^2 + 2x - 7 = 0",
    "What is the value of x in the equation 2^(x-1) + 2^(x+1) = 40?",
    "Solve the system of equations: {3x + 2y = 10, x - 3y = 5}",
    "Factorize the expression: x^4 - 16",
    "Determine the domain of the function f(x) = sqrt(4 - x^2)",
    "Simplify the expression: (sin(x) + cos(x))^2 - sin^2(x) - cos^2(x)",
    "Solve the equation: e^(2x) - 5e^x + 6 = 0",
    "Find the inverse function of f(x) = 3x^2 + 2x + 1",
    "Determine the discriminant of the quadratic equation: 2x^2 + 5x - 3 = 0",
    "What are the real roots of the equation: x^3 - 6x^2 + 11x - 6 = 0?",
    "Find the critical points of the function f(x) = x^4 - 4x^3 + 2x^2 - 5x + 3",
    "Solve the equation: sin(2x) + cos(x) = 0",
    "Find the equation of the tangent line to the curve y = x^3 - 2x^2 + x + 1 at the point (1, 1)",
    "Determine the range of the function g(x) = 2x^2 - 3x + 1",
    "Solve the system of equations: {3x + 2y - z = 10, x - y + 2z = 5, 2x + y - 3z = 4}",
    "Factorize the expression: x^4 - 10x^2 + 25",
    "Find the vertex of the parabola defined by the equation y = x^2 + 4x - 5",
    "Determine the intercepts of the line with equation 3x - 2y = 12",
    "Find the limit of the function f(x) = (x^2 - 4) / (x - 2) as x approaches 2",
    "Solve the system of equations: {x^2 + y^2 = 25, x + y = 7}",
    "Determine the maximum and minimum values of the function f(x) = x^3 - 3x^2 + 4x - 1",
    "Find the equation of the line passing through the points (1, 2) and (4, 5)",
    "Determine the vertex of the parabola defined by the equation y = -2x^2 + 4x + 3",
    "Find the point(s) of intersection of the curves y = x^2 - 4x + 3 and y = 2x - 1",
    "Solve the inequality: 2x^2 - 5x < 3",
    "Find the equation of the line perpendicular to y = 3x - 2 passing through the point (4, 5)",
    "Determine the distance between the lines 2x + 3y = 7 and 4x - y = 2",
    "Find the solution set of the inequality: |3x - 4| > 7",
    "Solve the system of equations: {2x + 3y + 4z = 10, 3x - 2y + z = 5, x + 4y - 2z = 7}",
    "Determine the area enclosed by the curves y = x^2 and y = 2x",
    "Find the general solution to the differential equation dy/dx = 3x^2 - 6x + 2"
]



def performance_evaluation():
    st.markdown("<h2 style='text-align: center; color: #ffff80;'>Performance Evaluation System</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #ffffb3;'>Elevate your knowledge in a way determined by Machine learning algorithms to empower your learning experince.</h4>", unsafe_allow_html=True)
    inner_selection_list = [1, 2, 3]
    ip1 = st.selectbox(
        "Define current question paper difficulty (Easy / Medium / Hard)",
        ["Easy", "Medium", "Hard"]
    )
    # ip1 = st.selectbox(
    #     "Enter the duration of test taken in hours:",
    #     inner_selection_list
    # )
    ip2 = st.selectbox(
        "On a scale of 1-3 rate your confidence with this test paper :",
        inner_selection_list
    )
    ip3 = st.selectbox(
        "Enter the duration of test taken in hours:",
        inner_selection_list
    )
    ip4 = st.selectbox(
        "Enter the Number of incorrect answers.(15, 20, 25) :",
        [15, 20, 25]
    )
    ip5 = st.selectbox(
        "Enter your attempt for this level of paper",
        inner_selection_list
    )
    if ip1 == "Easy":
        ip1 = 4
    if ip1 == "Medium":
        ip1 = 6.8
    if ip1 == "Hard":
        ip1 = 7
    if ip2 == 1:
        ip2 = 385
    if ip2 == 2:
        ip2 = 390
    if ip2 == 3:
        ip2 = 396
    if ip3 == 1:
        ip3 = 10
    if ip3 == 2:
        ip3 = 15
    if ip3 == 3:
        ip3 = 20
    if ip4 == 15:
        ip4 = 10
    if ip4 == 20:
        ip4 = 18
    if ip4 == 25:
        ip4 = 22
    if ip5 == 1:
        ip5 = 0
    if ip5 == 2:
        ip5 = 15
    if ip5 == 3:
        ip5 = 25

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    import numpy as np
    from joblib import load
    housing = pd.read_csv("data.csv")
    my_pipeline = Pipeline([
    # ('imputer', SimpleImputer(strategy="median")),
    #     ..... add as many as you want in your pipeline
    ('std_scaler', StandardScaler()),
    ])
    my_pipeline.fit_transform(housing)

    test = [[0.00632,ip3,ip5,0,0.538,ip1,65.2,4.09,1,296,ip4,ip2,4.98,24]]
    test2 = my_pipeline.transform(test)
    test3 = np.array([test2[0][:13]])
    model = load('Evaluator.joblib') 

    value = model.predict(test3)
    val = value[0]
    percent = val*100/35
    test_val = percent
    percent = "{:.2f}".format(percent)

    if st.button('Generate QP'):
        st.markdown("<h2 style='text-align: center; color: #ffff80;'>Performance Evaluation Report</h2>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: #ffff80;'>Based on your inputs the user readyness percentage to try next level is: </h6>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #ffff80;'>"+str(percent)+" % \rready</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #ffff80;'> Based on your performance you can try these questions</h2>", unsafe_allow_html=True)

        if test_val < 70:
            # st.text("Going with Easy level questions :")
            random_easy_questions = random.sample(easy_algebra_questions, 30)
            for i, question in enumerate(random_easy_questions, 1):
                st.text(f"Question {i}: {question}")
        elif test_val <90:
            # st.text("Going with Medium level questions :")
            random_medium_questions = random.sample(medium_algebra_questions, 30)
            for i, question in enumerate(random_medium_questions, 1):
                st.text(f"Question {i}: {question}")
        else:
            # st.text("Going with Hard level questions :")
            random_hard_questions = random.sample(hard_algebra_questions, 30)
            for i, question in enumerate(random_hard_questions, 1):
                st.text(f"Question {i}: {question}")



def base_page():
    st.markdown("<h6 style='text-align: center; color: red;'>&copy A combined final year project by Abhigyan Aman and team.</h6>", unsafe_allow_html=True)







pages = {
    "Landing Page" : base_page,
    "Course Reccomendation System" : course_recommendation,
    "Performance Evaluation System" : performance_evaluation
}

selection = st.sidebar.radio("Objective Navigator :", list(pages.keys()))
pages[selection]()