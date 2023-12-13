# InteriorDesign
Проект по созданию программы-дизайнера интерьера. 

Команда проекта:
cтуденты ИТМО
Лейтес Анна и 
Пахолков Виктор

В репозитории находятся следующие файлы:
ML System Design Doc - документ описывающий предпосылки и разработку ML системы
bedroom_labelled_sample.zip - сжатая папка с фотографиями спален
labelled_bedrooms_data_sample.txt - аннотация к фотографиям

а также программные файлы и файлы данных которые мы использовали на этапе исследования решений идеи. 

Мы присоединились на третьей недели курса (первой учебной неделе в университете), начав описывать наше видение в ML-дизайн-доке.

На четвертой неделе курса мы 
- Проработали идеи прототипа приложения для первых пользователей
-Попробовали запустить наиболее близкую по идее к нашему приложению text-to-room - во время её выполнения она заняла более 70 гб места на google colab. Код запуска в файле failed_text2room_test.ipynb
- Проверили возможности stable diffusion в работе. Код в файле Room_generator_trial_stable_diffusion_ipynb_.ipynb
- Выбрали результаты stable diffusion как baseline для сравнения в дльнейшей работе по улучшению качества результатов модели. Некоторые из картинок: appartment_plan.png, lvivng_room(2).png, planv1.png. 
- Добавили описание use cases в ML System Doc

На пятой неделе курса было сделано следующее:
- Разработан UI/UX дизайн прототипа веб сайта и реализован на streamlit. Файл Design.py
- Проведены проверки style transfer моделей на возможность их использования в поставленной задачес помощью предобученной VGG-19 для Style Transfering. Файлы interior_design_renovation.ipynb и interior_design_renovation.py 

- Добавили описание baseline  в ML System Doc, а также уточнили другие разделы в соответствии с изменившимися требованиями к системе

На шестой неделе курса: 
- Разработано видение pipeline работы системы в use case от текстового запроса до вывода результата работы программы.  Файл "Предварительная схема решения.jpeg"
- Добавлено это в ML System Doc
- Произвели поиск и анализ датасетов на которых могла бы обучать модель. Проверено более 10 потенциальных датасетов различающихся по входным-выходным данным, тематике и формату.
- Отправлены запросы на доступ к датасетам.

На седьмой неделе курса: 
- После получения обратной связи на семинаре мы заполнили Readme
- Пересмотрели бизнес-требования в ML- design doc и план MVP решения
- Подобрали датасет картинок комнат (часть этого датасета загрузили в Bedrooms_labelled_sample.zip)
- Разметили часть спален из вышеуказанного датасета (файл labelled_bedrooms_data_sample.txt). 

На восьмой неделе:
- разметили больше данных и добавили загрузчик данных dataloader.ipynb

На девятой неделе:
- написали код поиска похожих векторов с помощью косинусной метрики similarity of vectors.ipynb content_and_elements_jaccard_comparison.ipynb


На десятой неделе курса:
- Расширен датасет: добавлены данные ванных, а также гостинных
- Проведен анализ скорости выполнения кода поиска наиболее похожего описания изображения к запросу пользователя, написанного на прошлой неделе
- Проведен рефакторинг функций, переписаны некоторые методы, добавлено обучение w2v на датасете вместо использования предобученного
- Вышеперечисленные изменения в разы увеличивают скорость выполнения программы, а также затраты памяти


На 11 неделе курса:
-  составлен прототип работы программы в streamlit Design.py
- а также расширен датасет: добавлены новые данные - разметку обеденных комнат 




На 12 неделе курса:
- Проверили работу программы при разных запросах. Выяснилось, что кодировка в эмбеддинг предложения у запроса пользователя и в датасете выполняются по-разному (по-словам и по-словосочетаниям) 
- Стали использовать предобученную  модель для представления эмбедингов
- А также добавили словарь синонимов преобразования запроса с использованием синонимов из датасета synonyms_for_user_input.ipynb


На 13 неделе курса:
- Пременили эмбеденги с помощью трансформерных моделей (Bert), вычислили косинусное расстрояние Sentence_transformers.ipynb
- Работали над кастомным токенизатором 
- Реорганизовали программный код для удобства запуска разных версий и проведения экспериментов
  в папке desktop_app_version_0 файлы main.py, data_loader.py, preprocessing.py similarities.py
- В связи с реорганизацией дизайн дока, пересмотрели, что может быть бейзлайном и что этапом


На четырнадцатой неделе кусра:
- разработан back-end системы файл app.py
- разработан front-end системы, соединён с back-end'ом
папка desktop_app_version_0
