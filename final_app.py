import streamlit as st
from streamlit import components

st.set_page_config(
    page_title="INDIAN POLITICS : Topic Modelling & Sentiment Analysis",
    page_icon="https://live.staticflickr.com/65535/51212698633_3acc0d118f_c.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.title('INDIAN POLITICS : Topic Modelling & Sentiment Analysis')
'''
In the past decade, there has been a huge boom in data generation and analysis. Humongous amount of unstructured data is available in the forms of text documents, images, audios, emails and the most influential, social media data. 
Even if we narrow down to textual data, we are unable to process and gain hidden insights from it due to alarming rate of it’s generation. Thus, we need lucid pre-processing techniques and powerful algorithms to gain maximum information.
 
This is where Artificial Intelligence and Natural Language Processing come into play. We are going to focus on the textual data analytics and sentiment analysis applications of NLP.
Textual data analytics is a task used for processing text data to derive the high quality of information and to discover patterns from text. Sentiment analysis tries to identify and extract opinions within a given text across blogs, reviews, social media, forums, news etc.
Unleashing this power can prove to be a boon in many domains, ranging from finances to arts and education to politics. 

Through our study we intend to investigate the public opinion regarding the unique public relations campaign ‘Mann Ki Baat’ initiated by incumbent Prime Minister of India, Mr. Narendra Modi. Gaining insight into the campaign will be beneficial to the government, opposition parties as well as for academia.


In the framework proposed, our main intention is to gain useful insights into the 'Mann Ki Baat' speeches and also extract the sentiment attached with the public reviews regarding the same.
'''

# components.v1.html("""<html><head><meta name="description" content="_" /><meta name="title" property="og:title" content="_" />
#                    <meta property="og:type" content="_" /><meta name="image" property="og:image" content="https://live.staticflickr.com/65535/51212698633_3acc0d118f_c.jpg" />
#                    <meta name="description" property="og:description" content="_" /><meta name="author" content="Anushree Kolhe" /></head></html>""")


# from linkpreview import link_preview

# # url = "http://localhost"
# # content = """
# # <html><head><meta name="description" content="_" /><meta name="title" property="og:title" content="_" />
# #                    <meta property="og:type" content="_" /><meta name="image" property="og:image" content="https://live.staticflickr.com/65535/51212698633_3acc0d118f_c.jpg" />
# #                    <meta name="description" property="og:description" content="_" /><meta name="author" content="Anushree Kolhe" /></head></html>
# # """
# preview = link_preview("http://github.com/")
# print("title:", preview.title)
# print("description:", preview.description)
# print("image:", preview.image)
# print("force_title:", preview.force_title)
# print("absolute_image:", preview.absolute_image)
# preview = link_preview(url, content)
# print("title:", preview.title)
# print("description:", preview.description)
# print("image:", preview.image)
# print("force_title:", preview.force_title)
# print("absolute_image:", preview.absolute_image)


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