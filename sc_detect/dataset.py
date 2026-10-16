from pathlib import Path

import kagglehub
from loguru import logger
import typer

from sc_detect.config import RAW_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    competition_name: str = "isic-2024-challenge",
    output_dir: Path = RAW_DATA_DIR,
):
    # login
    logger.info("Realize o login no Kaggle:")
    kagglehub.login()
    logger.success("Login realizado com sucesso!")

    # download dos dados
    str_path = str(output_dir.resolve())  # a funcao espera receber uma string

    logger.info("Realizando o download dos dados...")
    kagglehub.competition_download(
        handle=competition_name,
        output_dir=str_path,
        force_download=True  # forcar atualizacao dos dados caso existam
    )
    logger.success("Download concluido com sucesso!")

if __name__ == "__main__":
    app()