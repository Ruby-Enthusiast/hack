import csv
from django.core.management.base import BaseCommand
from polls.models import CsvData

class Command(BaseCommand):
    help = 'Import data from questions.csv'

    def handle(self, *args, **options):
        # Change the path to the actual location of your questions.csv file
        csv_file_path = 'path/to/questions.csv'

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row

                for row in csv_reader:
                    # Assuming your CSV has columns 'category', 'question', 'code'
                    category, question, code = row
                    CsvData.objects.create(csv_category=category, csv_question=question, csv_code=code)

                self.stdout.write(self.style.SUCCESS('Successfully imported data from questions.csv'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file_path}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))