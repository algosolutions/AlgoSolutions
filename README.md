### Aglo Solution DataFeeds

Follow the steps below to get access to DataFeeds

- Install Dependencies from requirements.txt

- Download the config.py file and save in Project folder

- Run the DataFeeds.py file. Update the main() for relevant Symbols, startDate, and endDate. It should return 1 Minute price data of the company.

- Use Symbol Columns on the WIKI page - https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

```python
#Changes to DataFeeds.py File
if __name__ == '__main__':
    HistoricPrices1Min('AAPL', '2010-01-01', '2020-07-15')
    HistoricPrices1Min('MSFT', '2010-01-01', '2020-07-15')
    HistoricPrices1Min('XOM', '2010-01-01', '2020-07-15')
    HistoricPrices1Min('MMM', '2010-01-01', '2020-07-15')

```

<!--
**algosolutions/AlgoSolutions** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
