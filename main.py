from sys import exit

from project_data import goods_shop, goods_store
from utils import send_request, display_items, create_instances


def main():
    print('Привет! Программа имитирует движение товаров между складом и магазином\n'
          '\nДля отправки товаров нужно ввести сообщение\n'
          'Формат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 2 диван из склад в магазин\n'
          '\nДля остановки программы в любой момент введите "стоп"\n'
          'Для начала работы нажмите Enter')
    user_input = input()

    if user_input == 'стоп':
        exit()

    # Create Shop, Store
    shop, store = create_instances(goods_shop, goods_store)

    while True:
        # Display items in store and shop
        print(display_items(store=store, shop=shop))

        # Prompt user input and process it
        user_task = input('\nВведите запрос: ')
        print(send_request(user_task, shop, store))


if __name__ == '__main__':
    main()
