from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=100
        param surname: Describes last name of the author
        type surname: str max_length=100
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=100
    """
    name = models.CharField(blank=True, max_length=100)
    surname = models.CharField(blank=True, max_length=100)
    patronymic = models.CharField(blank=True, max_length=100)
    books = models.ManyToManyField('book.Book', related_name='author_books', blank=True)

    objects = models.Manager()

    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        return f"{self.name} {self.surname}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f"Author(id={self.pk})"

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        try:
            return Author.objects.get(pk=author_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=100
        param surname: Describes surname of the author
        type surname: str max_length=100
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=100
        :return: a new author object which is also written into the DB
        """
        if name and surname and patronymic:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        return {
            'id': self.pk,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=100
        param surname: Describes surname of the author
        type surname: str max_length=100
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=100
        :return: None
        """
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if patronymic:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()
