import unittest
import qrcode
import dotenv
import os
import sys

sys.path.append("./src/")
from sdqrcode.sdqrcode import init_and_generate_sd_qrcode


class TestGenerateSDQRCodeAuto(unittest.TestCase):
    def setUp(self) -> None:
        dotenv.load_dotenv("./tests/.env")

        return super().setUp()

    def test_generate_sd_qrcode_txt2img_auto(self):
        sd_qr_code,_ = init_and_generate_sd_qrcode(
            config_name_or_path="./src/sdqrcode/configs/default_auto.yaml",
            auto_api_hostname=os.getenv("AUTO_API_HOSTNAME"),
            auto_api_port=os.getenv("AUTO_API_PORT"),
            auto_api_https=os.getenv("AUTO_API_HTTPS") == "true",
            auto_api_username=os.getenv("AUTO_API_USERNAME"),
            auto_api_password=os.getenv("AUTO_API_PASSWORD"),
        )

        self.assertIsNotNone(sd_qr_code)

        for i, sd_qr_code_img in enumerate(sd_qr_code):
            sd_qr_code_img.save(
                f"./tests/imgs_test_results/test_generate_sd_qrcode_{i}_auto_txt2img.png"
            )

    def test_generate_sd_qrcode_img2img_auto(self):
        sd_qr_code, _ = init_and_generate_sd_qrcode(
            config_name_or_path="./src/sdqrcode/configs/img2img_tile_auto.yaml",
            auto_api_hostname=os.getenv("AUTO_API_HOSTNAME"),
            auto_api_port=os.getenv("AUTO_API_PORT"),
            auto_api_https=os.getenv("AUTO_API_HTTPS") == "true",
            auto_api_username=os.getenv("AUTO_API_USERNAME"),
            auto_api_password=os.getenv("AUTO_API_PASSWORD"),
        )

        self.assertIsNotNone(sd_qr_code)

        for i, sd_qr_code_img in enumerate(sd_qr_code):
            sd_qr_code_img.save(
                f"./tests/imgs_test_results/test_generate_sd_qrcode_{i}_auto_img2img.png"
            )


if __name__ == "__main__":
    unittest.main()
