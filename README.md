# ML Course 2026 — Lean Study Repo

Компактный учебный репозиторий по курсу ML: только задания, ноутбуки и нужные датасеты.

## Структура

- `exercises/` — все практические задания
  - `ex01/` — очистка данных (`ex01_ru.ipynb`, `dirty_dataset.csv`)
  - `ex01_extra/` — доп. анализ attrition (`ex01_extra_ru.ipynb`, IBM HR CSV)
  - `ex02/` — анализ `tips.csv`
  - `ex03/` — adults-кейс
  - `ex04_auto_mpg/` — регрессия на `auto-mpg.data`
  - `ex05_titanic/` — Titanic classification
  - `ex06_knn/` — KNN задание
  - `ex07_customers/` — customer segmentation
  - `week07_ann/` — ANN notebook
  - `week07_cnn/` — CNN notebook
- `docs/` — минимальная сопровождающая документация
  - `study_guide_ru.md`
  - `week7_submission_pack.md`

## Быстрый старт

1. Установить зависимости:
   - `pip install jupyter pandas numpy scikit-learn matplotlib seaborn`
2. Запустить Jupyter в корне репозитория:
   - `jupyter notebook`
3. Открыть нужный ноутбук из `exercises/` и запускать ячейки сверху вниз.

## Главный проект курса

**Water Quality EE** — классификация качества воды Эстонии по открытым данным Terviseamet.
Вынесен в отдельный репозиторий: [sapsan14/water-quality-ee](https://github.com/sapsan14/water-quality-ee)

## Принципы этого репозитория

- Один канонический ноутбук на одно задание.
- Где доступны обе языковые версии, храним обе: `*_ru.ipynb` и `*_et.ipynb`.
- Только необходимые данные рядом с ноутбуком.
- Без служебной инфраструктуры синхронизации и лишних дублей.
