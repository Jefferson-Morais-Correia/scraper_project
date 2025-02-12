import pandas as pd
#import os
#from scraper_project.utils.helpers import save_to_csv


def test_save_to_csv():
    """
    Testa se o DataFrame é salvo corretamente como arquivo CSV.
    """
    data = pd.DataFrame(
        {"Title": ["Title 1"], "Abstract": ["Abstract 1"], "References": ["Ref 1"]}
    )
    save_to_csv(data, "test_output.csv")

    assert os.path.exists("test_output.csv"), "O arquivo CSV não foi criado."
    os.remove("test_output.csv")
