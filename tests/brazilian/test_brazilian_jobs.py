from src.brazilian_jobs import read_brazilian_file

result = [
    {"salary": "2000", "title": "Maquinista", "type": "trainee"},
    {"salary": "3000", "title": "Motorista", "type": "full time"},
    {"salary": "4000", "title": "Analista de Software", "type": "full time"},
    {
        "salary": "1700",
        "title": "Assistente administrativo",
        "type": " full time",
    },
    {
        "salary": "1400",
        "title": "Auxiliar administrativo",
        "type": " full time",
    },
    {"salary": "1400", "title": "Auxiliar usinagem", "type": " full time"},
    {"salary": "1400", "title": "Auxiliar de padaria", "type": " full time"},
    {"salary": "1400", "title": "Analista Contábil", "type": " full time"},
    {"salary": "5000", "title": "Gerente comercial", "type": " full time"},
    {
        "salary": "4000",
        "title": "Analista de Departamento Pessoal",
        "type": " full time",
    },
    {
        "salary": "50000",
        "title": "Esportista de Futebol profissional",
        "type": " full time",
    },
    {"salary": "4000", "title": "Analista de crédito", "type": " full time"},
    {"salary": "3000", "title": "Pessoa Programadora", "type": " full time"},
    {"salary": "3000", "title": "Ux Designer", "type": " full time"},
    {
        "salary": " 1400",
        "title": "Auxiliar de manutenção",
        "type": " full time",
    },
]


def test_brazilian_jobs():
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv") == result
