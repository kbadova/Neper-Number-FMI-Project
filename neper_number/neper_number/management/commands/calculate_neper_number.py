from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """Calculates the neper number"""

    def print(self, obj):
        self.stdout.write(str(obj))

    def add_arguments(self, parser):
        parser.add_argument('-p', type=int,
                            help='Number of members in row')

        parser.add_argument("-t", "-threads", type=int, default='1',
                            help="Number of threads")

        parser.add_argument('-o', '-output', type=str, default='result.txt',
                            help='Name of output file')

        parser.add_argument('-q', '-quiet', type=str, default='False',
                            help='quiet mode')

    def handle(self, *args, **options):
        members = options.get('p')
        threads = options.get('t')
        output_name = options.get('o')
        quiet_mode = options.get('q')

        print(" {} members, {} threads, {} output_name, {}queet mode".format(members, threads, output_name, quiet_mode))
        print("here we implement the algorithm")
