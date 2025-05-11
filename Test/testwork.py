from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time

options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

# Укажи путь к chromedriver
service = Service(r"C:\Users\Sokol\PycharmProjects\Python for Selenium auto test\Test\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.booking.com/index.ru.html")
    wait = WebDriverWait(driver, 20)

    # Попробуем закрыть баннер cookies
    try:
        accept_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Принять все']"))
        )
        accept_btn.click()
        print("✅ Cookie-баннер закрыт")
    except:
        print("⚠️ Cookie-баннер не найден или уже закрыт")

    # Добавим паузу на всякий случай
    time.sleep(2)

    # Пробуем найти поле поиска
    search_input = wait.until(
        EC.presence_of_element_located((By.ID, "ss"))
    )
    print("✅ Поле ввода найдено")

    search_input.clear()
    search_input.send_keys("Москва")
    search_input.send_keys(Keys.ENTER)

    # Ждём результатов
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "f6431b446c")))
    results = driver.find_elements(By.CLASS_NAME, "f6431b446c")
    print(f"✅ Найдено отелей: {len(results)}")

except Exception as e:
    print("❌ Произошла ошибка:")
    traceback.print_exc()

finally:
    driver.quit()