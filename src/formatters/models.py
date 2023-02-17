"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class StatutoryActModel(BaseModel):
    """
Модель законов и нормативных актов:

.. code-block::

    StatutoryActModel(
    type="Конституция Российской Федерации",
    title="Наука как искусства",
    acceptance_date="01.01.2000",
    act_num="1234-56",
    source="Парламентская газета",
    year=2020,
    source_num=5,
    arcticle_num=15,
    editorial_date="11.09.2002",
    )
"""
    type: str
    title: str
    acceptance_date: str
    act_num: str
    source: str
    year: int = Field(..., gt=0)
    source_num: int = Field(..., gt=0)
    arcticle_num: int = Field(..., gt=0)
    editorial_date: str


class NewspaperArticleModel(BaseModel):
    """
    Модель статьи из газеты:

    .. code-block::

        NewspaperArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            newspaper_title="Южный Урал",
            year=1980,
            date="01.10"
            article_num=5,
        )
    """

    authors: str
    article_title: str
    newspaper_title: str
    year: int = Field(..., gt=0)
    date: str
    article_num: int = Field(..., gt=0)


class MagazineArticleModel(BaseModel):
    """
    Модель статьи из журнала:

    .. code-block::

        MagazineArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            magazine_title="Образование и наука",
            year=2020,
            magazine_num=10,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    magazine_title: str
    year: int = Field(..., gt=0)
    magazine_num: int = Field(..., gt=0)
    pages: str


class DissertationModel(BaseModel):
    """
    Модель диссертация:

    .. code-block::

        DissertationModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            dr_or_ph="д-р. / канд.",
            field="экон"
            code="01.01.01"
            city="СПБ"
            year=2020,
            pages=199,
        )
    """

    author: str
    title: str
    dr_or_ph: str
    field:str
    code:str
    city:str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)
