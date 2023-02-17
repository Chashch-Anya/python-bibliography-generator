"""
Запуск приложения.
"""
from enum import Enum, unique

from formatters.styles.gost import GOSTCitationFormatter
from formatters.styles.mla import MLACitationFormatter
from logger import get_logger
from readers.reader import SourcesReader,SourcesReaderMLA
from renderer import Renderer
from settings import INPUT_FILE_PATH, OUTPUT_FILE_GOST_PATH, OUTPUT_FILE_MLA_PATH

logger = get_logger(__name__)


@unique
class CitationEnum(Enum):
    """
    Поддерживаемые типы цитирования.
    """

    GOST = "gost"  # ГОСТ Р 7.0.5-2008
    MLA = "mla"  # Modern Language Association
    APA = "apa"  # American Psychological Association


def process_input(
    citation: str = CitationEnum.GOST.name,
    path_input: str = INPUT_FILE_PATH,
    path_output: str = OUTPUT_FILE_GOST_PATH,
) -> None:
    """
    Генерация файла Word с оформленным библиографическим списком (Формат ГОСТ Р 7.0.5-2008).

    :param str citation: Стиль цитирования
    :param str path_input: Путь к входному файлу
    :param str path_output: Путь к выходному файлу
    """

    logger.info(
        """Обработка команды с параметрами:
        - Стиль цитирования: %s.
        - Путь к входному файлу: %s.
        - Путь к выходному файлу: %s.""",
        citation,
        path_input,
        path_output,
    )

    models = SourcesReader(path_input).read()
    formatted_models = tuple(
        str(item) for item in GOSTCitationFormatter(models).format()
    )

    logger.info("Генерация выходного файла ...")
    Renderer(formatted_models).render(path_output)

    logger.info("Команда успешно завершена.")


def process_mla_input(
    citation: str = CitationEnum.MLA.name,
    path_input: str = INPUT_FILE_PATH,
    path_output: str = OUTPUT_FILE_MLA_PATH,
) -> None:
    """
    Генерация файла Word с оформленным библиографическим списком (Формат MLA).

    :param str citation: Стиль цитирования
    :param str path_input: Путь к входному файлу
    :param str path_output: Путь к выходному файлу
    """

    logger.info(
        """ Обработка команды с параметрами:
        - Стиль цитирования: %s.
        - Путь к входному файлу: %s.
        - Путь к выходному файлу: %s.""",
        citation,
        path_input,
        path_output,
    )

    models = SourcesReaderMLA(path_input).read()
    formatted_models = tuple(
        str(item) for item in MLACitationFormatter(models).format()
    )

    logger.info("Генерация выходного файла MLA...")
    Renderer(formatted_models).render(path_output)

    logger.info("Команда успешно завершена.")


if __name__ == "__main__":
    try:
        # запуск обработки входного файла для гост
        process_input()

        # запуск обработки входного файла для MLA
        process_mla_input()

    except Exception as ex:
        logger.error("При обработке команды возникла ошибка: %s", ex)
        raise
