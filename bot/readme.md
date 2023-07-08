# Products telegram bot
![telegram image](https://dssl.kz/wp-content/uploads/2019/08/95343281_w640_h640_trassir-telegrambot-prilozhenie-1100x1100.png)
### *Easiest solution for searching and filtering products*

Available commands

| command   | about                                                       |
|-----------|-------------------------------------------------------------|
| /low      | searching and sorting products from low price to high price |
| /high     | searching and sorting products from high price to low price |
| /custom   | custom searching products in price range                    |
| /history  | getting history of user queries                             |


### Configuring and run instructions

1. Clone repo to your computer
2. Create virtual environment using virtualenv application <br> `python -m virtualenv venv`
3. Activate your virtual env using activate file
4. Install requirements from requirements.txt file <br> `pip install -r requirements.txt`
5. Set up your telegram token in `.env.template` file and rename it into `.env`
6. Run project using `python main.py`

