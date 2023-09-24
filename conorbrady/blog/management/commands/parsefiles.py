from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Article, Label
import os
import datetime, pytz
from dotenv import load_dotenv
load_dotenv()
class Command(BaseCommand):


    def get_files(self):

        article_dir = os.environ['ARTICLE_DIR']
        records = []
        for path, dirs, files, in os.walk(article_dir):
            for file in files:
                if file[-3:] == '.md':
                    records.append(os.path.join(path, file))
        return records

    def parse_file(self, filename):

        with open(filename) as f:
            contents = f.read()

        _, header, *body = contents.split('---')
        body = '---'.join(body)

        header_lines = [h.strip() for h in header.split('\n') if h != '']
        header_obj = {}
        for hl in header_lines:
            key, value = hl.split(': ')
            if key == 'labels':
                values = value.split(', ')
            elif key == 'date':
                values = datetime.datetime.strptime(value, '%Y-%m-%d')
            else:
                values = value
            header_obj[key] = values

        return header_obj, body.strip()

    def last_modified(self, filename):
        mod_time = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(mod_time).replace(tzinfo=pytz.UTC)

    def handle(self, *args, **options):

        # Get Directory Listing / all md files
        md_files = self.get_files()
        # Get last_modified date of file
        for file in md_files:
            mod_time = self.last_modified(file)

            data, body = self.parse_file(file)

            # If slug doesn't exist or newer than last db entry, update db
            create_new = False
            try:
                result = Article.objects.filter(slug = data['slug']).latest('modified_date')
                if mod_time > result.modified_date:
                    create_new = True
                    result.active = False
                    result.save()
            except ObjectDoesNotExist:
                create_new = True

            if create_new:
                # If new file insert new record
                pub_date = data['date'].replace(tzinfo=pytz.UTC)
                new_article = Article(title = data['title'], slug = data['slug'],
                              pub_date = pub_date, modified_date = mod_time, body = body)
                new_article.save()
                # Labels
                for label in data['labels']:
                    try:
                        label_obj = Label.objects.get(name = label)
                    except ObjectDoesNotExist:
                        label_obj = Label(name = label)
                        label_obj.save()
                    new_article.labels.add(label_obj)

                new_article.save()
