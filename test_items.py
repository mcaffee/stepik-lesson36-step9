from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_page(browser, language):
    # given
    expected_texts = {
        'ar': 'أضف الى سلة التسوق',
        'ca': 'Afegeix a la cistella',
        'cs': 'Vložit do košíku',
        'da': 'Læg i kurv',
        'de': 'In Warenkorb legen',
        'en-gb': 'Add to basket',
        'el': 'Προσθήκη στο καλάθι',
        'es': 'Añadir al carrito',
        'fi': 'Lisää koriin',
        'fr': 'Ajouter au panier',
        'it': 'Aggiungi al carrello',
        'ko': '장바구니 담기',
        'nl': 'Voeg aan winkelmand toe',
        'pl': 'Dodaj do koszyka',
        'pt': 'Adicionar ao carrinho',
        'pt-br': 'Adicionar à cesta',
        'ro': 'Adauga in cos',
        'ru': 'Добавить в корзину',
        'sk': 'Pridať do košíka',
        'uk': 'Додати в кошик',
        # this lang doesn't work
        'zh-hans': 'Add to basket',
    }
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    # when
    browser.get(url)

    select = Select(browser.find_element_by_tag_name('select[name="language"]'))
    select.select_by_value(language)

    lang_btn = browser.find_element_by_xpath('//*[@id="language_selector"]/button')
    lang_btn.click()

    add_btn = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add_to_basket_form"]/button'))
    )
    actual_text = add_btn.text

    assert actual_text == expected_texts[language]
