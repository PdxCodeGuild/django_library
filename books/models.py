from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    title = models.CharField(max_length=128)
    published = models.DateField(blank=True, null=True)
    page_count = models.PositiveIntegerField()
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.author.full_name}'


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title}: {self.date}'