# EX01 — Очистка и обработка данных в Pandas

Русская версия. English version: [ASSIGNMENT_EX01.md](ASSIGNMENT_EX01.md)

**Курс:** TalTech ML for Engineers 2026  
**Moodle:** EX01 - Notebook Link (section id 146327)  
**Данные:** `dirty_dataset.csv` (не открывать в Excel перед использованием — это может изменить формат).

## Содержание

- [Цель](#цель)
- [Данные](#данные)
- [Шаги 1-15 (кратко)](#шаги-1-15-кратко)
- [Сдача](#сдача)
- [Ссылки на изображения (из ноутбука)](#ссылки-на-изображения-из-ноутбука)

---

## Цель

Привести в порядок CSV с кадровыми данными: загрузить, поправить имена и значения столбцов, добавить новые, отсортировать и сохранить. Использовать **Pandas**; выполнять шаги 1–15 в ноутбуке с **точными именами переменных** для автотеста.

## Данные

- **Файл:** `dirty_dataset.csv`
- **Разделитель:** `;`
- **Столбцы (исходные):** Id, Nimi1, Vanus, Liitumise_Kuupäev, Tööala, Palk, Parkimine
- **Проблемы:** смешанные форматы, пропуски, дубликаты, невалидный возраст/зарплата, названия отделов (Finance→FI, Ops→OP, HR, IT), форматы дат.

## Шаги 1-15 (кратко)

1. **Загрузка** — В Colab смонтировать Drive; задать `path` к CSV. Читать `pd.read_csv(path, sep=";")` в `df`.
2. **Обзор** — `df.info()`, `df.head()`, `df.tail()`, `df.describe()`, проверка дубликатов и пропусков.
3. **Имена столбцов** — Копия в `df_col_rename`. Переименовать: Tööala→Amet, Liitumise_Kuupäev→Liitumise_kuupäev.
4. **Имена** — Копия в `df_name`. Разбить полное имя на Eesnimi и Perekonnanimi.
5. **Возраст** — Копия в `df_age`. Импутация, отбор допустимых значений, целый тип.
6. **Даты** — Копия в `df_date`. Привести к одному формату и pd.to_datetime().
7. **Зарплата** — Копия в `df_salary`. Импутация, целый тип.
8. **Удалить Parkimine** — Копия в `df_dropped`, удалить столбец Parkimine.
9. **Отдел (Amet)** — Копия в `df_title`. Только FI, OP, HR, IT; маппинг и импутация.
10. **Дубликаты** — Копия в `df_dupl`. Удалить дубликаты по (Eesnimi, Perekonnanimi), оставить первое.
11. **Новые столбцы** — `df_dt`: Aastat_liitumisest; `df_cat`: Palk_kategooria (madal/keskmine/kõrge).
12. **Слияние с зданиями** — Таблица df_hoone (Id, Hoone), merge → `df_merged`.
13. **Сортировка** — `df_sort`: по Liitumise_kuupäev по убыванию, reset_index.
14. **Порядок столбцов** — `df_col_sorted`: Id, Liitumise_kuupäev, Aastat_liitumisest, Amet, Eesnimi, Perekonnanimi, Palk, Palk_kategooria, Vanus.
15. **Сохранение** — Сохранить CSV, index=False.

## Сдача

- Финальный запуск в **Google Colab**.
- Имя ноутбука: **EX01.ipynb**.
- Доступ: **Anyone with the link** — **Viewer**.
- Эту ссылку отправить в Moodle (EX01 - Notebook Link).

---

## Ссылки на изображения (из ноутбука)

- Step 3: [03_veergude_nimetamine.png](https://cs.taltech.ee/services/forge/maksim.tsopov/itx0020-images/raw/branch/main/ex01_pandas/03_veergude_nimetamine.png)  
- Step 4: [04_nimede_lahutamine.png](https://cs.taltech.ee/services/forge/maksim.tsopov/itx0020-images/raw/branch/main/ex01_pandas/04_nimede_lahutamine.png)  
- Steps 5–14: [5_age.png … 14_veergude_tostmine.png](https://cs.taltech.ee/.../ex01_pandas/new/5_age.png)  

Используйте их для проверки ожидаемых названий столбцов и значений (если есть доступ).
