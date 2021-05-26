import streamlit as st
from streamlit import components

st. set_page_config(layout="wide")
st.title('INDIAN POLITICS : Topic Modelling & Sentiment Analysis')

'''
## Gensim LDA 
### Optimal number of topics
'''
col1, col2 = st.beta_columns([5,5])
with col1:
    st.image('Images/Gensim_topic1.png', caption='No. of iterations = 8', width=650)

with col2:
    st.image('Images/Gensim_topic2.png', caption='No. of iterations = 10', width=650)

'''
### No. of topics = 6
'''
HtmlFile = open("HTML/gensim_lda1_viz.html", 'r', encoding='utf-8')
lda_viz1 = HtmlFile.read() 
print(lda_viz1)
components.v1.html(lda_viz1, width=1250, height=900, scrolling=True)


'''
## Mallet LDA 
'''
HtmlFile = open("Images/Mallet_topics.html", 'r', encoding='utf-8')
lda_viz2 = HtmlFile.read() 
print(lda_viz2)
components.v1.html(lda_viz2, width=1100, height=650, scrolling=True)

'''
### No. of topics = 7
'''
HtmlFile = open("HTML/mallet_lda.html", 'r', encoding='utf-8')
lda_viz3 = HtmlFile.read() 
print(lda_viz3)
components.v1.html(lda_viz3, width=1250, height=900, scrolling=True)

'''
### Speech wise dominant topic
'''
col1, mid, col2 = st.beta_columns([4,1,4])
with col1:
    st.image('Images/docs_topics_monthly.png', width=600)
with col2:
    st.image('Images/docs_topics_yearly.png', width=500)

HtmlFile = open("Images/Mallet_all_topics.html", 'r', encoding='utf-8')
lda_viz4 = HtmlFile.read() 
print(lda_viz4)
components.v1.html(lda_viz4, width=1200, height=500, scrolling=True)





'''
## Sentiment Analysis
### Most commonly used words in the tweets
'''
st.image('Images/cleaned.png', width=600)

'''
### SentiWordNet (Lexicon based) model
'''
HtmlFile = open("Images/senti_word_review.html", 'r', encoding='utf-8')
senti1 = HtmlFile.read() 
print(senti1)
components.v1.html(senti1, width=1200, height=500, scrolling=True)

'''
### Comparision of Naive Bayes and SVM classifiers
'''
col1, mid, col2 = st.beta_columns([4,1,4])
with col1:
    st.image('Images/roc_nb.png', width=600)
with col2:
    st.image('Images/roc_svm.png', width=600)

'''
## Sentiments associated with each topic
'''    
HtmlFile = open("Images/sentiment&topics_reviews.html", 'r', encoding='utf-8')
senti1 = HtmlFile.read() 
print(senti1)
components.v1.html(senti1, width=1200, height=500, scrolling=True)