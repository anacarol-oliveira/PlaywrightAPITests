import os
import json
from datetime import datetime
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv


load_dotenv()


class BaseClient:

    BASE_URL = os.getenv("BASE_URL")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    TOKEN = None

    @staticmethod
    def save_logs(method, endpoint, payload, response, params=None):

        current_test = os.environ.get("PYTEST_CURRENT_TEST")

        if not current_test:
            return

        test_path = current_test.split("::")[0]

        normalized_path = test_path.replace("\\", "/")

        path_parts = normalized_path.split("/")

        specs_index = path_parts.index("specs")

        feature = path_parts[specs_index + 1]
        method_folder = path_parts[specs_index + 2]

        test_file = path_parts[-1].replace(".py", "")

        log_dir = os.path.join(
            "logs",
            feature,
            method_folder
        )

        os.makedirs(log_dir, exist_ok=True)

        log_path = os.path.join(
            log_dir,
            f"log_{test_file}.txt"
        )

        separator = "=" * 80

        with open(log_path, "w", encoding="utf-8") as log:

            log.write(f"\n{separator}\n")

            log.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n"
            )

            log.write(f"\nTEST FILE: {test_file}")
            log.write(f"\nMETHOD: {method}")
            log.write(f"\nENDPOINT: {endpoint}")
            log.write(f"\nSTATUS CODE: {response.status}\n")

            if params:

                log.write("\nQUERY PARAMS:\n")

                log.write(
                    f"{json.dumps(params, indent=4, ensure_ascii=False)}\n"
                )

            if payload:

                log.write("\nREQUEST BODY:\n")

                log.write(
                    f"{json.dumps(payload, indent=4, ensure_ascii=False)}\n"
                )

            log.write("\nRESPONSE BODY:\n")

            try:

                log.write(
                    f"{json.dumps(response.json(), indent=4, ensure_ascii=False)}\n"
                )

            except Exception:

                log.write(f"{response.text()}\n")

    @staticmethod
    def get_token():

        if BaseClient.TOKEN:
            return BaseClient.TOKEN

        with sync_playwright() as p:

            request = p.request.new_context()

            response = request.post(
                f"{BaseClient.BASE_URL}/auth/login",
                data={
                    "email": BaseClient.EMAIL,
                    "password": BaseClient.PASSWORD
                },
                headers={
                    "Content-Type": "application/json"
                }
            )

            response_json = response.json()

            if "access_token" not in response_json:

                raise Exception(
                    f"Erro ao gerar token: {response_json}"
                )

            BaseClient.TOKEN = response_json["access_token"]

            return BaseClient.TOKEN

    @staticmethod
    def post(endpoint, payload):

        token = BaseClient.get_token()

        with sync_playwright() as p:

            request = p.request.new_context()

            response = request.post(
                f"{BaseClient.BASE_URL}{endpoint}",
                data=json.dumps(payload),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}"
                }
            )

            try:

                body = response.json()

            except Exception:

                body = response.text()

            BaseClient.save_logs(
                method="POST",
                endpoint=endpoint,
                payload=payload,
                response=response
            )

            return {
                "status_code": response.status,
                "body": body,
                "headers": response.headers
            }

    @staticmethod
    def get(endpoint, params=None):

        token = BaseClient.get_token()

        with sync_playwright() as p:

            request = p.request.new_context()

            response = request.get(
                f"{BaseClient.BASE_URL}{endpoint}",
                params=params,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}"
                }
            )

            try:

                body = response.json()

            except Exception:

                body = response.text()

            BaseClient.save_logs(
                method="GET",
                endpoint=endpoint,
                payload=params if params else {},
                response=response,
                params=params
            )

            return {
                "status_code": response.status,
                "body": body,
                "headers": response.headers
            }

    @staticmethod
    def patch(endpoint, payload):

        token = BaseClient.get_token()

        with sync_playwright() as p:

            request = p.request.new_context()

            response = request.patch(
                f"{BaseClient.BASE_URL}{endpoint}",
                data=json.dumps(payload),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}"
                }
            )

            try:

                body = response.json()

            except Exception:

                body = response.text()

            BaseClient.save_logs(
                method="PATCH",
                endpoint=endpoint,
                payload=payload,
                response=response
            )

            return {
                "status_code": response.status,
                "body": body,
                "headers": response.headers
            }

    @staticmethod
    def delete(endpoint):

        token = BaseClient.get_token()

        with sync_playwright() as p:

            request = p.request.new_context()

            response = request.delete(
                f"{BaseClient.BASE_URL}{endpoint}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}"
                }
            )

            try:

                body = response.json()

            except Exception:

                body = response.text()

            BaseClient.save_logs(
                method="DELETE",
                endpoint=endpoint,
                payload={},
                response=response
            )

            return {
                "status_code": response.status,
                "body": body,
                "headers": response.headers
            }