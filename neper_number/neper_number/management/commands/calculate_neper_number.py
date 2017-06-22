import math
import datetime

from multiprocessing import Process, Queue
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

    def calculate_member(k, res):
        member_res = ((3 * k) * (3 * k) + 1) / math.factorial(3 * k)
        res.put(member_res)

    def calculate_sum(self, members, threads):
        res = Queue()
        list_of_k = {i: list() for i in range(threads)}
        for k in range(members):
            thread = k % 6
            list_of_k[thread].append(k)

        '''
        {0: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96], 1: [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97], 2: [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98], 3: [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99], 4: [4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94], 5: [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95]}
        '''
        for t in list_of_k:
            for k in list_of_k[t]:
                p = Process(target=calculate_member,
                            args=(k, res))
                p.start()

        neper_number = sum([res.get() for _ in range(0, threads)])

    def handle(self, *args, **options):
        members = options.get('p')
        threads = options.get('t')
        output_name = options.get('o')
        quiet_mode = options.get('q')

        start_time = datetime.now()

        result = self.calculate_row(members, threads)

        end_time = datetime.now()

        time_taken = end_time - start_time

        print("time taken is {}".fomrat(time_taken))
        print("result is {}".fomrat(result))

        print(" {} members, {} threads, {} output_name, {}queet mode".format(members, threads, output_name, quiet_mode))
        print("here we implement the algorithm")
