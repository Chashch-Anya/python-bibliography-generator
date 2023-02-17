"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel
from formatters.models import ArticlesCollectionModel, MagazineArticleModel, NewspaperArticleModel, DissertationModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class GOSTBook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. – $edition$city: $publishing_house, $year. – $pages с."
        )

    def substitute(self) -> str:

        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class GOSTInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article // $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:

        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class GOSTCollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $collection_title. – $city: $publishing_house, $year. – С. $pages."
        )

    def substitute(self) -> str:

        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTNewspaperArticle(BaseCitationStyle):
    """
    Форматирование для статьи из газеты.
    """

    data: NewspaperArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $newspaper_title. $year. $date. С. $article_num."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи из газеты "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            newspaper_title=self.data.newspaper_title,
            year=self.data.year,
            date=self.data.date,
            article_num=self.data.article_num,
        )


class GOSTMagazineArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала
    """

    data: MagazineArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $magazine_title. $year. $magazine_num. С.$pages"
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи из журнала "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            magazine_title=self.data.magazine_title,
            year=self.data.year,
            magazine_num=self.data.magazine_num,
            pages=self.data.pages,
        )


class GOSTDissertation(BaseCitationStyle):
    """
    Форматирование для диссертации
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $title: $dr_or_ph $city, $year. $pages c."
        )

    def substitute(self) -> str:

        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(
            author=self.data.author,
            title=self.data.title,
            dr_or_ph=self.data.dr_or_ph,
            field=self.data.field,
            code=self.data.code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        NewspaperArticleModel.__name__:GOSTNewspaperArticle,
        MagazineArticleModel.__name__:GOSTMagazineArticle,
        DissertationModel.__name__:GOSTDissertation,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
