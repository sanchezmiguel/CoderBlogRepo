from blogApp.forms import ArticuloForm, CardSearchForm
from django.test import TestCase
from django.contrib.auth.models import User
from blogApp.models import Articulo


class ArticuloModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea un usuario de prueba
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_user.save()

    def setUp(self):
        # Configuración inicial para cada prueba
        author = User.objects.get(id=1)
        self.articulo = Articulo.objects.create(
            title='Título de prueba',
            subtitle='Subtítulo de prueba',
            text='Texto de prueba',
            image='ruta/de/imagen.jpg',
            author=author
        )

    def test_title_max_length(self):
        max_length = self.articulo._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_subtitle_max_length(self):
        max_length = self.articulo._meta.get_field('subtitle').max_length
        self.assertEquals(max_length, 200)

    def test_text_blank(self):
        field = self.articulo._meta.get_field('text')
        self.assertTrue(field.blank)

    def test_image_upload_to(self):
        upload_to = self.articulo._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'articulo_images/')

    def test_str_representation(self):
        self.assertEquals(str(self.articulo), self.articulo.title)

    def test_author_relationship(self):
        author = self.articulo.author
        self.assertTrue(isinstance(author, User))
        self.assertEquals(author.username, 'testuser')

    def test_verbose_name(self):
        self.assertEquals(Articulo._meta.verbose_name, "Artículo")

    def test_verbose_name_plural(self):
        self.assertEquals(Articulo._meta.verbose_name_plural, "Artículos")


class ArticuloFormTest(TestCase):

    def test_form_fields(self):
        form = ArticuloForm()
        self.assertTrue('title' in form.fields)
        self.assertTrue('subtitle' in form.fields)
        self.assertTrue('text' in form.fields)
        self.assertTrue('image' in form.fields)

    def test_form_labels(self):
        form = ArticuloForm()
        self.assertEquals(form.fields['title'].label, 'Título')
        self.assertEquals(form.fields['subtitle'].label, 'Subtítulo')
        self.assertEquals(form.fields['text'].label, 'Texto del artículo')
        self.assertEquals(form.fields['image'].label, 'Imagen')


class CardSearchFormTest(TestCase):

    def test_form_fields(self):
        form = CardSearchForm()
        self.assertTrue('search_text' in form.fields)

    def test_form_labels(self):
        form = CardSearchForm()
        self.assertEquals(form.fields['search_text'].label, 'Search Text')

    def test_form_widgets(self):
        form = CardSearchForm()
        self.assertEquals(form.fields['search_text'].widget.attrs['placeholder'], 'Enter search text')

    def test_form_max_length(self):
        form = CardSearchForm()
        self.assertEquals(form.fields['search_text'].max_length, 100)

    def test_form_required(self):
        form = CardSearchForm()
        self.assertFalse(form.fields['search_text'].required)


class ArticuloListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.articulo = Articulo.objects.create(title='Test Article', subtitle='Test Subtitle', text='Test Text',
                                                author=self.user)

