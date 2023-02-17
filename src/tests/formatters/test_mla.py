"""
Тестирование функций оформления списка источников по MLA.
"""
from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel,ArticlesCollectionModel
from formatters.styles.mla import MLABook, MLAInternetResource,MLACollectionArticle


class TestMLA:
    """
    Тестирование оформления списка источников согласно MLA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = MLABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н.. Наука как искусство. СПб., Просвещение, 2020"
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = MLAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство. Ведомости, https://www.vedomosti.ru. Дата обращения 01.01.2021."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = MLACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Сборник научных трудов. – СПб.: АСТ, 2020. – С. 25-30."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        models = [
            MLABook(book_model_fixture),
            MLAInternetResource(internet_resource_model_fixture),
            MLACollectionArticle(articles_collection_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[2]
        assert result[1] == models[0]
        assert result[2] == models[1]

