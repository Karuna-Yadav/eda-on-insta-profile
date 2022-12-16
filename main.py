import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title('Top 1000 Instagram Influencers')
st.markdown('''This app shows Top 1000 Instagram Influencers till february 2022
by the number of quality and engaged followers
Find top Instagram accounts in any country and 
industry to make the most of your marketing campaigns. ''')
df = pickle.load(open("df_new.pkl", 'rb'))
data = pd.DataFrame.from_dict(df)
st.header("Instagram Audience ")
st.markdown('''Found that out of the Top 1,000 Instagram influencers
 have the United States,Indonesia,Mexico,Brazil And India as
Top 5 audience country. where, ''')
st.markdown(" - 29% audience is from United States")
st.markdown(" - 16% audience is from Brazil")
st.markdown(" - 14% audience is from India ")
st.markdown(" - 13% audience is from Indonesia")
st.markdown(" - 5% audience is from Mexico")
fig = plt.figure(figsize=(35, 10))
sns.countplot(x="Audience Country", data=data)
plt.title("Relative Frequency of Audience Country", fontsize=20)
plt.xlabel("Audience Country", fontsize=20)
plt.ylabel("Count", fontsize=20)
st.pyplot(fig)
st.header("Categories")
st.markdown('''The largest number of top Audience are located in the USA.
The reason for the greatest popularity of instagram from the United States 
lies in the active socio-cultural position of this country,
most of the stars of modern cinema live in the United States. 
India is in second place. The reason lies in the large population. 
The absence of China in this ranking is due to the high level of state 
censorship and the high prevalence of local social networks. 
Interestingly, several of the top ranked Instagram accounts
globally were under the category "Photography",but this category was not found in 
the top followers or audience engagement for the United States, Brazil, Indonesia, Mexico''')
col1, col2 = st.columns(2)
with col1:
    topfollowers = data.nlargest(10, 'Followers')
    fig1 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers.Category, topfollowers.Followers, label='Followers', width=0.8, color='skyblue')
    plt.xticks(fontsize=12, rotation=85)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Category", fontsize=16)
    plt.title("TOP 10 CATEGORIES BY FOLLOWERS ", fontsize=20)
    plt.tight_layout()
    st.pyplot(fig1)
with col2:
    topfollowers20 = data.nlargest(20, 'Followers')
    fig2 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers20.Category, topfollowers20.Followers, label='Followers', width=0.8, color='Chartreuse')
    plt.xticks(fontsize=12, rotation=85)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Category", fontsize=16)
    plt.title("TOP 20 CATEGORIES BY FOLLOWERS ", fontsize=20)
    plt.tight_layout()
    st.pyplot(fig2)
df_usa = data[data['Audience Country'] == 'United States']
df_ind = data[data['Audience Country'] == 'India']
df_bra = data[data['Audience Country'] == 'Brazil']
df_indo = data[data['Audience Country'] == 'Indonesia']
df_mex = data[data['Audience Country'] == 'Mexico']
st.markdown("- The top  categories by followers in the United States were:")
topfollowers_usa = df_usa.nlargest(10, 'Followers')
df1 = topfollowers_usa.pivot_table(index="Category", values="Followers", aggfunc=['sum'], sort=False)
st.table(data=df1)
st.text('''Here 40% of these groups have "Fashion", 40% have "Music", 20% 
have "Modeling", 20% have "Beauty", 20% have "Lifestyle",
20% have "Clothing", and 20% have "Outfits".''')
st.markdown("- The top  categories by followers in the Brazil were:")
topfollowers_bra = df_bra.nlargest(10, 'Followers')
df2 = topfollowers_bra.pivot_table(index="Category", values="Followers", aggfunc=['sum'], sort=False)
st.table(data=df2)
st.text('''Here 44% of these groups have "Sports", 39% have "Music", 9% 
have "Cinema", 6% have "Humor".''')
st.markdown("- The top  categories by followers in the India were:")
topfollowers_ind = df_ind.nlargest(10, 'Followers')
df3 = topfollowers_ind.pivot_table(index="Category", values="Followers", aggfunc=['sum'], sort=False)
st.table(data=df3)
st.text(''' Here 39% of these group have "Sports", 33% have "Photography",
 26% have "Cinema", 17% have "Music"''')
st.markdown("- The top  categories by followers in the Indonesia were:")
topfollowers_indo = df_indo.nlargest(10, 'Followers')
df4 = topfollowers_indo.pivot_table(index="Category", values="Followers", aggfunc=['sum'], sort=False)
st.table(data=df4)
st.text(''' Here 56% of these group have "Music & lifestyle",17% have "Sports",
9% have "Humor",9% have "Shows", 7% have "Cinema". ''')
st.markdown("- The top  categories by followers in the Mexico were:")
topfollowers_mex = df_mex.nlargest(10, 'Followers')
df5 = topfollowers_mex.pivot_table(index="Category", values="Followers", aggfunc=['sum'], sort=False)
st.table(df5)
st.text(''' Here 77% of these group have "Music", 15% have "Cinema",
15% have Clothing, 7% have "Humor". ''')
st.markdown('''From the above Tables, we can see the categories on Sports,
Music, Lyfestyle and Cinema is having more followers overall. ''')
col1, col2 = st.columns(2)
with col1:
    fig9 = plt.figure(figsize=(12, 8))
    plt.hist(df_usa.Followers, color='royalblue', range=(0, 60000000))
    plt.xlabel('Followers', fontsize=16)
    plt.ylabel('Number of Instagram Accounts', fontsize=16)
    plt.title('Histogram: Follower Counts of Top Instagram Accounts in the US', fontsize=20)
    st.pyplot(fig9)
with col2:
    fig7 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers_usa.Account, topfollowers_usa.Followers, label='Followers', width=0.8, color='Orchid')
    plt.xticks(fontsize=12, rotation=90)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Account", fontsize=16)
    plt.title("Top 10 account by Followers in usa", fontsize=20)
    st.pyplot(fig7)
col1, col2 = st.columns(2)
with col1:
    ff2 = plt.figure(figsize=(12, 8))
    plt.hist(df_ind.Followers, color='hotpink', range=(0, 60000000))
    plt.xlabel('Followers', fontsize=16)
    plt.ylabel('Number of Instagram Accounts', fontsize=16)
    plt.title('Histogram: Follower Counts of Top Instagram Accounts in the INDIA', fontsize=20)
    st.pyplot(ff2)
with col2:
    fig5 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers_ind.Account, topfollowers_ind.Followers, label='Followers', width=0.8, color='MediumPurple')
    plt.xticks(fontsize=12, rotation=90)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Account", fontsize=16)
    plt.title("Top 10 account by Followers in India", fontsize=22)
    st.pyplot(fig5)
col1, col2 = st.columns(2)
with col1:
    ff3 = plt.figure(figsize=(12, 8))
    plt.hist(df_bra.Followers, color='MediumVioletRed', range=(0, 60000000))
    plt.xlabel('Followers', fontsize=16)
    plt.ylabel('Number of Instagram Accounts', fontsize=16)
    plt.title('Histogram: Follower Counts of Top Instagram Accounts in the BRAZIL', fontsize=20)
    st.pyplot(ff3)
with col2:
    fig8 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers_bra.Account, topfollowers_bra.Followers, label='Followers', width=0.8, color='MediumPurple')
    plt.xticks(fontsize=12, rotation=90)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Account", fontsize=16)
    plt.title("Top 10 account by Followers in Brazil", fontsize=22)
    st.pyplot(fig8)
col1, col2 = st.columns(2)
with col1:
    ff1 = plt.figure(figsize=(12, 8))
    plt.hist(df_indo.Followers, color='orange', range=(0, 60000000))
    plt.xlabel('Followers', fontsize=16)
    plt.ylabel('Number of Instagram Accounts', fontsize=16)
    plt.title('Histogram: Follower Counts of Top Instagram Accounts in the INDONESIA', fontsize=20)
    st.pyplot(ff1)
with col2:
    fig3 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers_indo.Account, topfollowers_indo.Followers, label='Followers', width=0.8, color='steelblue')
    plt.xticks(fontsize=12, rotation=90)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Account", fontsize=16)
    plt.title("Top 10 account by Followers in Indonesia", fontsize=22)
    st.pyplot(fig3)
col1, col2 = st.columns(2)
with col1:
    ff = plt.figure(figsize=(12, 8))
    plt.hist(df_usa.Followers, color='MediumPurple', range=(0, 60000000))
    plt.xlabel('Followers', fontsize=16)
    plt.ylabel('Number of Instagram Accounts', fontsize=16)
    plt.title('Histogram: Follower Counts of Top Instagram Accounts in the Mexico', fontsize=22)
    st.pyplot(ff)
with col2:
    fig6 = plt.figure(figsize=(12, 8))
    plt.bar(topfollowers_mex.Account, topfollowers_mex.Followers, label='Followers', width=0.8, color='cadetblue')
    plt.xticks(fontsize=12, rotation=90)
    plt.ylabel("Followers", fontsize=16)
    plt.xlabel("Account", fontsize=16)
    plt.title("Top 10 account by Followers in Mexico", fontsize=22)
    st.pyplot(fig6)
st.text('''From the Visualization we conclude that Indian Audience 
is having Accounts with Most followings ''')
fig4 = plt.figure(figsize=(15, 5))
sns.scatterplot(x="Engagement avg", y="Followers", data=data)
plt.title("Followers Vs Engagement Rate")
st.pyplot(fig4)
st.markdown("Engagement is propotional to followers")
