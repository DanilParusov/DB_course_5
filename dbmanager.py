import psycopg2

from creation import HH, DB
from config import config

def formation():
    """Функция делает все запросы, создеёт базу данных и таблицы,"""
    hh = HH()
    Company_ID = hh.get_request()
    Vacancies = hh.get_id(Company_ID)
    db = DB()
    db.create_database()
    db.save_data_to_database(Company_ID, Vacancies)


class DBManager:
    """Класс подключаться к БД Postgres для вывода информации """
    def __init__(self):
        self.config = config()

    def connect_to_db(self):
        """Формирует запрос в Базе Данных"""
        conn = psycopg2.connect(dbname='course_work', **self.config)
        return conn

    def get_companies_and_vacancies_count(self) -> None:
        """Получает список всех компаний и количество вакансий у каждой компании."""
        conn = self.connect_to_db()
        with conn.cursor() as cur:
            cur.execute("SELECT company_name, company_open_vacansies FROM company")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_all_vacancies(self) -> None:
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        conn = self.connect_to_db()
        with conn.cursor() as cur:
            cur.execute("""SELECT vacancies, company_name, salary, url_vacancy
                        FROM vacancy
                        JOIN company USING(company_id)""")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_avg_salary(self) -> None:
        """Получает среднюю зарплату по вакансиям."""
        conn = self.connect_to_db()
        with conn.cursor() as cur:
            cur.execute("""SELECT ROUND(AVG(salary), 2) FROM vacancy
                           WHERE salary NOT IN ('0')""")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        conn = self.connect_to_db()
        with conn.cursor() as cur:
            cur.execute("""SELECT company_name, vacancies, salary, url_vacancy  
                            FROM vacancy
                            JOIN company USING(company_id)
                           WHERE salary > (SELECT AVG(salary) FROM vacancy WHERE salary != 0)""")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_keyword(self, word) -> None:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        conn = self.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(f"""SELECT company_name, vacancies, salary, url_vacancy  
                            FROM vacancy
                            JOIN company USING(company_id)
                            WHERE vacancies LIKE '%{word.capitalize()}%'""")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.commit()
        conn.close()