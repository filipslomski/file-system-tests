import random
import string


class DataGenerator:

    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]

    def __init__(self, context):
        self.context = context
        self.logger = context.logger

    def random_number_with_n_digits(self, n: int) -> int:
        lower = 10 ** (n - 1)
        upper = 10 ** n - 1
        generated_number = random.randint(lower, upper)
        self.logger.info(f'Number generated: {generated_number}')

        return generated_number

    def random_string(self, length: int = 10, chars=string.ascii_letters + string.digits) -> str:
        generated_string = ''.join(random.choice(chars) for _ in range(length))
        self.logger.info(f'String generated: {generated_string}')

        return generated_string

    def random_unique_string(self, length: int = 10, chars=string.ascii_letters + string.digits) -> str:
        generated_string = ""
        while length > 0:
            if (random_letter := random.choice(string.ascii_letters)) not in generated_string:
                generated_string += random_letter
                length -= 1
        self.logger.info(f'Unique string generated: {generated_string}')

        return generated_string

    def random_password(self) -> str:  # 8 chars+, 1 upper, 1 lower, 1 special, 1 number, no more than 2 repeating chars
        special_characters = "!@#$%^&*-?"
        password_required_part = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + \
            random.choice(string.digits) + random.choice(special_characters)
        password_random_part = self.random_unique_string(random.randint(4, 6))
        self.logger.info(f'Password generated: {password_required_part + password_random_part}')

        return password_required_part + password_random_part

    def random_element(self, elements: list):
        return random.choice(elements)

    def random_email(self):
        return f"{self.random_string(7,chars=string.ascii_lowercase)}@{random.choice(self.domains)}"
