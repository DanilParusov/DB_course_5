from dbmanager import DBManager, formation

if __name__ == "__main__":
    bdm = DBManager()
    formation()
    print(bdm.get_companies_and_vacancies_count())
    while True:
        print("Приветствую тебя пользователи в данной программе мы сможем отобразить тебе вакансии 10 самых топовых it-компаний России")
        print("1: получает список всех компаний и количество вакансий у каждой компании.")
        print("2: получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.")
        print("3: получает среднюю зарплату по вакансиям.")
        print("4: получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.")
        print("5: получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.")
        user_input = int(input("Выбери число от 1 до 5"))
        if user_input == 1:
            print(bdm.get_companies_and_vacancies_count())
        elif user_input == 2:
            print(bdm.get_all_vacancies())
        elif user_input == 3:
            print(bdm.get_avg_salary())
        elif user_input == 4:
            print(bdm.get_vacancies_with_higher_salary())
        elif user_input == 5:
            word = input("Введите слово по которому вы хотите найти вакансии")
            print(bdm.get_vacancies_with_keyword(word))
